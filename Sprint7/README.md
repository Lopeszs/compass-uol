# Exercícios

## Lab AWS Glue

### Etapa 1: Preparando os dados de origem
![Etapa1](exercicios/Lab_AWS_Glue/etapa_1.webp)
<br></br>

### Etapa 2: Configurando sua conta para utilizar o AWS Glue
![Etapa2](exercicios/Lab_AWS_Glue/etapa_2.webp)<br></br>

### Etapa 3: Criando a IAM Role para os jobs do AWS Glue
![Etapa3](exercicios/Lab_AWS_Glue/etapa_3.webp)<br></br>

### Etapa 4: Configurando as permissões no AWS Lake Formation
![Etapa4.1](exercicios/Lab_AWS_Glue/etapa_4.1.webp)<br></br>
![Etapa4.2](exercicios/Lab_AWS_Glue/etapa_4.2.webp)<br></br>

### Etapa 5: Criando novo job no AWS Glue
![Etapa5](exercicios/Lab_AWS_Glue/etapa_5.webp)<br></br>

### Etapa 5.2: Sua vez!
O código pode ser verificado [aqui](exercicios/Lab_AWS_Glue/script.py)   

### Resultado da execução no Bucket S3
![Etapa5.2_bucket](exercicios/Lab_AWS_Glue/etapa_5.2_bucket.webp)<br></br>

#### Exemplo de arquivo json gerado:
![Etapa5.2_arquivo](exercicios/Lab_AWS_Glue/etapa_5.2_arquivo.webp)<br></br>

### Log da execução
![Etapa5.2_log](exercicios/Lab_AWS_Glue/etapa_5.2_log.webp)<br></br>

### Etapa 6: Criando novo crawler
![Etapa6](exercicios/Lab_AWS_Glue/etapa_6.webp)<br></br>

#### Analisando a tabela no Glue Catalog:
![Glue Catalog](exercicios/Lab_AWS_Glue/glue_catalog.webp)<br></br>

#### Analisando os dados no Amazon Athena:
![Athena](exercicios/Lab_AWS_Glue/athena.webp)<br></br>



## Apache Spark - Contador de Palavras

### Etapa 1: Realizar o pull da imagem jupyter/all-spark-notebook
![Etapa1](exercicios/Apache_Spark/etapa_1.webp)<br></br>

### Etapa 2: Criar um container a partir da imagem
![Etapa2](exercicios/Apache_Spark/etapa_2.webp)<br></br>

#### Acessando o Jupyter Lab
![Etapa2.1](exercicios/Apache_Spark/etapa_2.1.webp)<br></br>

### Etapa 3: Acessando o terminal do container
![Etapa3](exercicios/Apache_Spark/etapa_3.webp)<br></br>

### Etapa 4: Contar palavras no README.md do repositório Git

Primeiramente, no terminal do container em execução, usei o comando curl -O (URL do README.md no Git), incluindo o token temporário, para baixar o arquivo README.md para o container. Após o download, usei o comando cat para verificar se o arquivo foi baixado corretamente:
![Etapa4](exercicios/Apache_Spark/etapa_4.webp)<br></br>

Com o arquivo baixado com sucesso, iniciei o PySpark para realizar a análise no README.md:
![Etapa4.1](exercicios/Apache_Spark/etapa_4.1.webp)<br></br>  

Em seguida, inseri a sequência de comandos Spark necessários para contar as ocorrências de cada palavra presente no arquivo README.md e obtive um resultado satisfatório:
![Etapa4.2](exercicios/Apache_Spark/etapa_4.2.webp)<br></br>

O script python também foi testado no jupyter Lab, o código e os resultados podem ser conferidos [aqui](exercicios/Apache_Spark/script.ipynb)

# Certificados

- Data & Analytics - PB - AWS - Novo - 7/10
![Data & Analytics - PB - AWS - Novo - 7/10](certificados/Data&Analytics7.jpg)<br></br>
