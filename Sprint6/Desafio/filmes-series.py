import zipfile
import boto3
import os
from datetime import datetime
from dotenv import load_dotenv

# Caminho do arquivo zip 
zip_file_path = "filmes-series.zip"

# Função para extrair os arquivos do arquivo ZIP
def extract_zip(zip_file, extract_to="."):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

# Extrair o arquivo zip na pasta atual
extract_zip(zip_file_path)

# Carrega variáveis de ambiente do arquivo .env (credenciais)
load_dotenv()

# Definição das variáveis
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_session_token = os.getenv("AWS_SESSION_TOKEN")
bucket_name = "data-lake-filmes-series" # Nome do Bucket
raw_zone = "Raw" # Nome da zona RAW no S3
local_source = "Local" # Fonte local dos arquivos a serem enviados
data_format = "CSV" # Formato dos arquivos
movies_folder = "Movies" # Pasta para armazenar arquivos de filmes
series_folder = "Series" # Pasta para armazenar arquivos de séries
current_date = datetime.now().strftime("%Y/%m/%d") # Formata a data atual para "YYYY/MM/DD"

# Caminhos dos arquivos CSV extraídos
movies_file_path = "movies.csv"
series_file_path = "series.csv"

# Configuração do cliente S3 com boto3
s3 = boto3.client("s3",
                  aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key,
                  aws_session_token=aws_session_token)

# Função para upload de arquivos CSV para o S3
def upload_file_to_s3(file_path, bucket, destination_path):
    s3.upload_file(file_path, bucket, destination_path)

# Define os caminhos no S3 para os arquivos, seguindo o padrão de armazenamento
s3_movies_path = os.path.join(raw_zone, local_source, data_format, movies_folder, current_date, "movies.csv")
s3_series_path = os.path.join(raw_zone, local_source, data_format, series_folder, current_date, "series.csv")

# Faz o upload dos arquivos CSV para o S3 utilizando a função
upload_file_to_s3(movies_file_path, bucket_name, s3_movies_path)
upload_file_to_s3(series_file_path, bucket_name, s3_series_path)

# Comandos Docker
# docker build -t img-filmes-series . ## Constrói a imagem docker
# docker run --name filmes-series --env-file .env -v filmes_volume:/app/data img-filmes-series ## Executa um container a partir da imagem criada
