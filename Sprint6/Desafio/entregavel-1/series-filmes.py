import zipfile
import boto3
import os
from datetime import datetime
from dotenv import load_dotenv

# Caminho do arquivo zip no repositório
zip_file_path = "filmes-series.zip"

# Função para extrair os arquivos do arquivo ZIP
def extract_zip(zip_file, extract_to="."):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

# Extrair o arquivo zip na pasta atual
extract_zip(zip_file_path)

# Agora os arquivos movies.csv e series.csv estarão disponíveis
movies_file_path = "movies.csv"
series_file_path = "series.csv"

# O resto do seu código continua igual
# Carrega variáveis de ambiente do arquivo .env (credenciais)
load_dotenv()

# Definição das variáveis de configuração
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_session_token = os.getenv("AWS_SESSION_TOKEN")
bucket_name = "data-lake-filmes-series"
raw_zone = "Raw"
local_source = "Local"
data_format = "CSV"
movies_folder = "Movies"
series_folder = "Series"
current_date = datetime.now().strftime("%Y/%m/%d")

# Configuração do cliente S3 com boto3
s3 = boto3.client("s3",
                  aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key,
                  aws_session_token=aws_session_token)

# Função para upload de arquivos CSV para o S3
def upload_file_to_s3(file_path, bucket, destination_path):
    s3.upload_file(file_path, bucket, destination_path)

# Definir os caminhos no S3 com base no padrão de armazenamento
s3_movies_path = os.path.join(raw_zone, local_source, data_format, movies_folder, current_date, "movies.csv")
s3_series_path = os.path.join(raw_zone, local_source, data_format, series_folder, current_date, "series.csv")

# Fazer o upload dos arquivos CSV para o S3
upload_file_to_s3(movies_file_path, bucket_name, s3_movies_path)
upload_file_to_s3(series_file_path, bucket_name, s3_series_path)

# Comandos Docker
# docker build -t img-filmes-series . ## Constrói a imagem docker
# docker run --name filmes-series --env-file .env -v filmes_volume:/app/data img-filmes-series ## Executa um container a partir da imagem criada
