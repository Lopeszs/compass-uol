from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import expr, row_number
from pyspark.sql.window import Window

# Caminhos de origem e destino dos dados
source_local = "s3://data-lake-filmes-series/Trusted/Local/Parquet/Movies/2024/11/21/"
source_tmdb = "s3://data-lake-filmes-series/Trusted/TMDB/Parquet/Movies/2024/11/21/"
destino_dim_filme = "s3://data-lake-filmes-series/Refined/dim_filme"
destino_fato_avaliacao = "s3://data-lake-filmes-series/Refined/fato_avaliacao"
destino_dim_ator = "s3://data-lake-filmes-series/Refined/dim_ator"

# Inicialização dos contextos Spark e Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init("job_name", {})

# Leitura dos arquivos Parquet
csv = spark.read.parquet(source_local)
json = spark.read.parquet(source_tmdb)

# Criação da "dimensão filme"
dim_filme = json.join(csv, json["imdb_id"] == csv["id"]) \
    .select(
        json["imdb_id"].alias("id_filme"),
        csv["tituloPrincipal"].alias("titulo"),
        csv["genero"].alias("genero")
    ).distinct()

# Criação da "dimensão ator" com ID único por nome e genero
dim_ator = csv.select(
    csv["nomeArtista"].alias("nome"),
    csv["generoArtista"].alias("genero"),
).distinct()  # Remover duplicatas para garantir um ator por nome e genero

# Criação do ID do ator
window_ator = Window.orderBy("nome")  # Remover partitionBy para garantir ID único para cada ator
dim_ator = dim_ator.withColumn("id_ator", row_number().over(window_ator))

# Criação do "fato avaliacao"
fato_avaliacao = json.join(csv, json["imdb_id"] == csv["id"]) \
    .join(dim_ator, csv["nomeArtista"] == dim_ator["nome"], "inner") \
    .select(
        json["imdb_id"].alias("id_filme"),
        dim_ator["id_ator"],
        csv["numeroVotos"].alias("numero_votos"),
        csv["notaMedia"].alias("nota_media"),
        csv["anoLancamento"].alias("ano_lancamento"),
        json["popularidade"].alias("popularidade")
    )

# Adicionando a coluna de IDs na tabela fato_avaliacao
window_fato = Window.orderBy("id_filme", "id_ator")
fato_avaliacao = fato_avaliacao.withColumn("id_avaliacao", row_number().over(window_fato))

# Reduzindo o número de partições para 1
dim_filme = dim_filme.coalesce(1)
fato_avaliacao = fato_avaliacao.coalesce(1)
dim_ator = dim_ator.coalesce(1)

# Salvando as tabelas em formato Parquet e registrando no catálogo de dados
dim_filme.write.format("parquet").mode("overwrite").option("path", destino_dim_filme).saveAsTable("datalake.dim_filme")
fato_avaliacao.write.format("parquet").mode("overwrite").option("path", destino_fato_avaliacao).saveAsTable("datalake.fato_avaliacao")
dim_ator.write.format("parquet").mode("overwrite").option("path", destino_dim_ator).saveAsTable("datalake.dim_ator")

job.commit()
