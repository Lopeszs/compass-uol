import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType
from pyspark.sql.functions import col, when
from datetime import datetime

# Inicializando argumentos e contexto
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Especificando os caminhos de entrada e saída
input_path = "s3://data-lake-filmes-series/Raw/Local/CSV/Movies/2024/10/28/movies.csv"

current_date = datetime.now()
year = current_date.strftime("%Y")
month = current_date.strftime("%m")
day = current_date.strftime("%d")
output_path = f"s3://data-lake-filmes-series/Trusted/Local/Parquet/Movies/{year}/{month}/{day}/"

# Definindo o schema dos dados
schema = StructType([
    StructField("id", StringType(), True),
    StructField("tituloPrincipal", StringType(), True),
    StructField("tituloOriginal", StringType(), True),
    StructField("anoLancamento", IntegerType(), True),
    StructField("tempoMinutos", IntegerType(), True),
    StructField("genero", StringType(), True),
    StructField("notaMedia", FloatType(), True),
    StructField("numeroVotos", IntegerType(), True),
    StructField("generoArtista", StringType(), True),
    StructField("personagem", StringType(), True),
    StructField("nomeArtista", StringType(), True),
    StructField("anoNascimento", IntegerType(), True),
    StructField("anoFalecimento", IntegerType(), True),
    StructField("profissao", StringType(), True),
    StructField("titulosMaisConhecidos", StringType(), True)
])

# Carregando os dados e aplicando o schema
df = spark.read.format("csv").option("sep", "|").schema(schema).load(input_path)

# Removendo duplicatas por combinação de 'id' e 'nomeArtista'
unique_df = df.drop_duplicates(['id', 'nomeArtista'])

# Convertendo valores '\N' para None em todas as colunas necessárias
df_cleaned = unique_df.select(
    *[when(col(c) == "\\N", None).otherwise(col(c)).alias(c) for c in unique_df.columns]
)

# Filtrando para manter apenas os filmes de Comédia ou Animação lançados após 1990
filtered_df = df_cleaned.filter(
    (col("genero").rlike("Animation|Comedy")) & (col("anoLancamento") > 1990)
)

# Coalescendo o DataFrame e escrevendo em formato Parquet
filtered_df.coalesce(1).write.mode("overwrite").parquet(output_path)

job.commit()
