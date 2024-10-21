import boto3
import os
import pandas as pd
import pandasql as psql
from io import StringIO
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env (credenciais)
load_dotenv()

# Variáveis para as credenciais AWS
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_session_token = os.getenv("AWS_SESSION_TOKEN") 

bucket_name = 'bucket-sprint5-anvisa' # Nome do Bucket
file_key = 'DADOS_ABERTOS_PRODUTO_FUMIGENO.csv' # Caminho pro arquivo CSV
arquivo_modificado_key = 'CONSULTA_DADOS_ABERTOS_PRODUTO_FUMIGENO.csv' # Resultado da consulta do arquivo CSV
local_file_path = 'DADOS_ABERTOS_PRODUTO_FUMIGENO.csv' # Caminho pro arquivo CSV


# Configuração do cliente S3 com boto3
s3 = boto3.client("s3",
                  aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key,
                  aws_session_token=aws_session_token)

# Função para upload de arquivos CSV para o S3
def upload_file_to_s3(file_path, bucket, destination_path):
    s3.upload_file(file_path, bucket, destination_path)

# Função para carregar o arquivo do S3
def carregar_arquivo_s3(bucket_name, file_key):
    obj = s3.get_object(Bucket=bucket_name, Key=file_key)
    conteudo = obj['Body'].read().decode('utf-8')
    return conteudo

# Função para executar a consulta SQL
def executar_consulta_sql(df):
    query = """
    SELECT 
        CATEGORIA AS CATEGORIA_PRODUTO,
        NUM_PRODUTOS_DISTINTOS,
        STATUS,
        DT_VENCIMENTO_REGISTRO,
        EMPRESA,
        NUM_PRODUTOS_POR_EMPRESA,
        NUM_PROCESSO
    FROM (
        SELECT 
            DS_CATEGORIA_PRODUTO AS CATEGORIA,
            COUNT(DISTINCT NO_PRODUTO) AS NUM_PRODUTOS_DISTINTOS,
            CASE 
                WHEN ST_SITUACAO_REGISTRO = 'Ativo' THEN 'Ativo'
                ELSE 'Inativo'
            END AS STATUS,
            STRFTIME('%Y-%m-%d', SUBSTR(DT_VENCIMENTO_REGISTRO, 7, 4) || '-' || SUBSTR(DT_VENCIMENTO_REGISTRO, 1, 2) || '-' || SUBSTR(DT_VENCIMENTO_REGISTRO, 4, 2)) AS DT_VENCIMENTO_REGISTRO,
            UPPER(NO_RAZAO_SOCIAL_EMPRESA) AS EMPRESA,
            CAST(NU_PROCESSO AS INTEGER) AS NUM_PROCESSO
        FROM df
        WHERE ST_SITUACAO_REGISTRO = 'Ativo'
            AND STRFTIME('%Y-%m-%d', SUBSTR(DT_VENCIMENTO_REGISTRO, 7, 4) || '-' || SUBSTR(DT_VENCIMENTO_REGISTRO, 1, 2) || '-' || SUBSTR(DT_VENCIMENTO_REGISTRO, 4, 2)) < DATE('now')
        GROUP BY DS_CATEGORIA_PRODUTO, ST_SITUACAO_REGISTRO, DT_VENCIMENTO_REGISTRO, NO_RAZAO_SOCIAL_EMPRESA
    ) AS subquery
    JOIN (
        SELECT 
            NO_RAZAO_SOCIAL_EMPRESA,
            COUNT(DISTINCT NO_PRODUTO) AS NUM_PRODUTOS_POR_EMPRESA
        FROM df
        WHERE ST_SITUACAO_REGISTRO = 'Ativo'
        GROUP BY DS_CATEGORIA_PRODUTO, NO_RAZAO_SOCIAL_EMPRESA
    ) AS empresa_count ON subquery.EMPRESA = empresa_count.NO_RAZAO_SOCIAL_EMPRESA
    ORDER BY NUM_PRODUTOS_DISTINTOS DESC
    """

    # Executa a consulta SQL usando pandasql
    resultado = psql.sqldf(query, locals())
    return resultado

# Função para salvar o DataFrame modificado no S3
def salvar_arquivo_s3(df, bucket_name, file_key):
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    
    s3.put_object(Bucket=bucket_name, Key=file_key, Body=csv_buffer.getvalue())

# Upload do arquivo CSV para o S3
upload_file_to_s3(local_file_path, bucket_name, file_key)

# Carrega o arquivo do S3
conteudo_csv = carregar_arquivo_s3(bucket_name, file_key)

# Cria o DataFrame
df = pd.read_csv(StringIO(conteudo_csv), delimiter=';')

# Executa a consulta SQL
df_resultado = executar_consulta_sql(df)

# Salva o DataFrame modificado no bucket S3
salvar_arquivo_s3(df_resultado, bucket_name, arquivo_modificado_key)
