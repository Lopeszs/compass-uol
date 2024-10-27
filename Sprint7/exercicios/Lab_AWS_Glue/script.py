import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql.functions import upper
from awsglue.dynamicframe import DynamicFrame

# Iniciar contexto Glue
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
logger = glueContext.get_logger()

# Ler dados do arquivo CSV a partir do parâmetro de entrada
input_path = args['S3_INPUT_PATH']
datasource0 = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [input_path]},
    format="csv",
    format_options={"withHeader": True}
)

# Imprimir o schema
datasource0.printSchema()

# Converter DynamicFrame para DataFrame
dataframe = datasource0.toDF()

# Alterar a caixa dos valores da coluna 'nome' para MAIÚSCULO
dataframe = dataframe.withColumn('nome', upper(dataframe['nome']))

# Imprimir a contagem de linhas
num_registros = dataframe.count()
logger.info(f"Número total de registros: {num_registros}")

# Contagem de nomes agrupados por ano e sexo, ordenando por ano
grouped_count = dataframe.groupBy('ano', 'sexo').count().orderBy('ano')

# Logar a contagem de nomes agrupados
for row in grouped_count.collect():
    logger.info(f"Ano: {row['ano']}, Sexo: {row['sexo']}, Total: {row['count']}")

# Nome feminino com mais registros
feminino_max = dataframe.filter(dataframe['sexo'] == 'F').groupBy('nome').count().orderBy('count', ascending=False).first()
logger.info(f"Nome feminino mais comum: {feminino_max['nome']} em {feminino_max['count']} registros.")

# Nome masculino com mais registros
masculino_max = dataframe.filter(dataframe['sexo'] == 'M').groupBy('nome').count().orderBy('count', ascending=False).first()
logger.info(f"Nome masculino mais comum: {masculino_max['nome']} em {masculino_max['count']} registros.")

# Total de registros por ano, limitando a 10
total_registros_por_ano = grouped_count.limit(10)
for row in total_registros_por_ano.collect():
    logger.info(f"Ano: {row['ano']}, Sexo: {row['sexo']}, Total: {row['count']}")

# Escrever conteúdo do dataframe no S3
output_path = args['S3_TARGET_PATH']
glueContext.write_dynamic_frame.from_options(
    frame=DynamicFrame.fromDF(dataframe, glueContext, "output_dynamic_frame"),
    connection_type="s3",
    connection_options={"path": output_path, "partitionKeys": ["sexo", "ano"]},
    format="json"
)

logger.info("Processamento concluído, dados salvos em formato JSON.")
