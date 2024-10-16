import boto3

# Substitua pelos seus dados
aws_access_key_id = 'ASIATX3PH6HQTC3XFYVV'  # Sua chave de acesso
aws_secret_access_key = 'KBx/A5PtvplimrscteaSzo9lwcuYHsI/PDMh0RSi'  # Sua chave secreta
aws_session_token = 'IQoJb3JpZ2luX2VjEJX//////////wEaCXVzLWVhc3QtMSJHMEUCIQDW6cJlZss9UgWLiejfsnPfEytFS6J26YeygrrXHEn02gIgIuHES9ipr/Ajjy08wu36haNunOoS5d+6tUsklZDc7PEqqAMI7v//////////ARAAGgwyNTczOTQ0NzEzOTMiDPHElXwXioSIJoUgaCr8AtZ7QhUF1W8QAZ2hbBDG5pNwoQk6Y2FNzBZOrpkTwzMPCJeOADIfmGmhembbmZQZr9h+RHbgLgPT6bmZhkPRWiW4MGN0nUj2VdyXluZRkXCkJyrA1UYeKlcIETkPjOTxxL1MmUADMom300xRw5n/FyXCXNC1sFbB7+GhdIWZ+EgTg6nQ9apBjLl6Kmn51rKeepfatLBr+NPk35x37aSx6LqRBcpdL6QPVaJjmvu49aK2/DndW5ItcjkW1tlt7qv4H9ftaW65kboIXI/oBZirx5NirL29uvZ4id/dzjin25xGAyOKcxwZacNabTCov9MGQXPJIsrlKepm6rKz9KO6/O/SBW7kJPYFF9r4stRhtwsQzHyQPRQitzrBms7gnx/oArUCevvU4SLRyOU9vHayjHASvNj2WlKPq52rnwqSLCo3aLUuavqj0zL3bFcZHwGJM7L6jBYCDGcEWr6eoGJEonUwg++QIRGzQS8SG6xlIZSHDplS79Y9evGQPPcPMK7FubgGOqYBe+dSg0omfusMZOrQGXN8R7+JbCcq36TLmXbvjjneAA//R/oO8Ktbrg9HRWU7nflAXA83pnd+R120nbLNlBJYDPN9mUptO9rDtYfVjGFMMCo6ero+LwTD7KoB//eJGWlIeSHbNbjVI971ifRIcYCuW4vHzvseyK2Uw+nFK/eNvdq/3NuSoKYHw1Kg/YeeIjR2fvYdMpsDfkTWb4bIivbbKbiYkhVkTA=='

def s3_select_query(bucket_name, file_name):
    # Crie uma sessão do Boto3
    session = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        aws_session_token=aws_session_token  # Adicione se necessário
    )

    # Crie uma instância do cliente S3 usando a sessão
    s3 = session.client('s3')

    # Defina a consulta SQL que você deseja executar
    query = """
    SELECT COUNT(*) AS total_processos, MAX(CAST(DT_VENCIMENTO_REGISTRO AS DATE)) AS data_max_vencimento, MIN(CAST(DT_VENCIMENTO_REGISTRO AS DATE)) AS data_min_vencimento FROM S3Object WHERE DS_CATEGORIA_PRODUTO = 'FUMO PARA NARGUILE'
    """

    # Execute a consulta usando S3 Select
    response = s3.select_object_content(
        Bucket=bucket_name,
        Key=file_name,
        ExpressionType='SQL',
        Expression=query,
        InputSerialization={
            'CSV': {
                'FileHeaderInfo': 'USE',  # Indica que o CSV contém um cabeçalho
                'FieldDelimiter': ';'      # Especifica o delimitador do seu CSV
            }
        },
        OutputSerialization={'CSV': {}},  # A resposta também será formatada como CSV
    )

    # Exibir os resultados da consulta
    for event in response['Payload']:
        if 'Records' in event:
            print(event['Records']['Payload'].decode('utf-8'))
        elif 'Stats' in event:
            print(event['Stats'])
        elif 'End' in event:
            print("Consulta concluída.")

# Substitua pelo nome do seu bucket e do arquivo CSV
bucket_name = 'bucket-sprint5-anvisa'  # Nome do seu bucket
file_name = 'DADOS_ABERTOS_PRODUTO_FUMIGENO.csv'  # Nome do seu arquivo

# Execute a função de consulta
s3_select_query(bucket_name, file_name)
