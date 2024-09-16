# Define a imagem base como Python 3
FROM python:3

# Define o diretório de trabalho dentro do container. 
WORKDIR /app

# Copia o mascarar-dados.py do diretório local para o /app
COPY mascarar-dados.py .

# Comando executado quando o container for iniciado
CMD ["python", "mascarar-dados.py"]