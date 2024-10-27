# Baseia-se na imagem do AWS Lambda para Python 3.8
FROM public.ecr.aws/lambda/python:3.8

# Cria um diretório para a instalação das dependências
WORKDIR /var/task

# Copia o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instala as dependências dentro do diretório 'python'
RUN pip install -r requirements.txt -t python/
