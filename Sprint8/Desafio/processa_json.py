import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F
from pyspark.sql.functions import when
from pyspark.sql.types import IntegerType
from datetime import datetime

# Inicializando o contexto do Glue
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminho de entrada e saída
input_path = "s3://data-lake-filmes-series/Raw/TMDB/JSON/2024/11/10/"
current_date = datetime.now()
year = current_date.strftime("%Y")
month = current_date.strftime("%m")
day = current_date.strftime("%d")
output_path = f"s3://data-lake-filmes-series/Trusted/TMDB/Parquet/Movies/{year}/{month}/{day}/"

# Leitura dos arquivos JSON com a opção multiline habilitada
df = spark.read.option("multiline", "true").json(input_path)

# Transformando colunas vazias "" em valores nulos
for col_name in df.columns:
    if dict(df.dtypes)[col_name] == "string":
        df = df.withColumn(col_name, when(df[col_name] == "", None).otherwise(df[col_name]))

# Selecionando e transformando colunas conforme sua lista
df_transformed = df.select(
    F.col("id"),
    F.col("title").alias("tituloPrincipal"),
    F.col("original_title").alias("tituloOriginal"),
    F.year("release_date").alias("anoLancamento"),
    F.col("runtime").cast(IntegerType()).alias("tempoMinutos"),
    
    # Convertendo lista de gêneros em string separada por vírgula
    F.concat_ws(",", F.expr("transform(genres, x -> x.name)")).alias("genero"),
    
    F.col("vote_average").alias("notaMedia"),
    F.col("vote_count").alias("numeroVotos"),
    
    # Produção das empresas de produção como string separada por vírgula
    F.concat_ws(",", F.expr("transform(production_companies, x -> x.name)")).alias("produtoras"),
    
    # Produção dos países como string separada por vírgula
    F.concat_ws(",", F.expr("transform(production_countries, x -> x.name)")).alias("paisProducao")
)

# Removendo registros sem ID, garantindo que os IDs sejam únicos e coalescendo para um único arquivo
df_cleaned = df_transformed.filter(df['id'].isNotNull()).dropDuplicates(["id"]).coalesce(1)

# Salvando o DataFrame final em formato Parquet
df_cleaned.write.mode("overwrite").parquet(output_path)

# Concluindo o job do Glue
job.commit()
