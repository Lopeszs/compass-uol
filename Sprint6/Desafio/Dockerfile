# Define a imagem base a ser utilizada como uma imagem oficial do Python versão 3
FROM python:3

# Define o diretório de trabalho dentro do container como /app. 
WORKDIR /app

# Copia os arquivos necessários para o diretório /app do container
COPY . /app

# Instala as dependências necessárias
RUN pip install boto3 python-dotenv

# Define o comando padrão para executar o script Python
CMD ["python", "filmes-series.py"]
