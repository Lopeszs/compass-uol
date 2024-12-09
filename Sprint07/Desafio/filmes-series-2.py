import json
import requests
import pandas as pd
import boto3
import os
from datetime import datetime

def lambda_handler(event=None, context=None):
    # Inicialização do cliente S3 e configuração de variáveis
    S3_CLIENT = boto3.client('s3')
    BUCKET = 'data-lake-filmes-series'
    API_KEY = os.environ['TMDB_API_KEY']
    current_date = datetime.now().strftime("%Y/%m/%d")  # Formato da data atual para o S3

    # Lê o CSV com filmes do IMDB armazenado no S3
    objeto = S3_CLIENT.get_object(Bucket=BUCKET, Key='Raw/Local/CSV/Movies/2024/10/23/movies.csv')
    filmes_imdb = pd.read_csv(objeto['Body'], sep='|', low_memory=False)

    # Filtro para filmes de comédia lançados a partir de 1990
    filmes_imdb['anoLancamento'] = filmes_imdb['anoLancamento'].replace('\\N', '0')
    imdb_filtro = filmes_imdb[ 
        (filmes_imdb.genero.str.contains("Animation|Comedy", regex=True)) & 
        (filmes_imdb['anoLancamento'].astype(int) >= 1990)
    ]

    tmdb_data = []  # Lista para armazenar os dados do TMDB
    processed_ids = set()  # Conjunto para armazenar os IDs dos filmes processados
    file_index = 0  # Contador de arquivos
    file_path = f'Raw/TMDB/JSON/{current_date}/filmes_{file_index}.json'  # Caminho inicial do arquivo

    # Passa por cada filme filtrado do CSV, pegando o ID e usando para descobrir o ID correspondente no TMDB
    for filme in imdb_filtro.values:
        id_imdb = filme[0]

        # Verifica se o ID do filme já foi processado
        if id_imdb in processed_ids:
            print(f"Filme {id_imdb} já processado, pulando...")
            continue

        # Acha o filme no TMDB com base no ID do IMDB 
        url = f"https://api.themoviedb.org/3/find/{id_imdb}?api_key={API_KEY}&language=pt-BR&external_source=imdb_id"
        response = requests.get(url)
        data = response.json()

        # Verifica se a lista de resultados não está vazia
        if data.get('movie_results'):
            id_tmdb = data['movie_results'][0]['id']

            # Faz uma segunda requisição para pegar mais detalhes sobre o filme
            url = f"https://api.themoviedb.org/3/movie/{id_tmdb}?api_key={API_KEY}&language=pt-BR"
            response = requests.get(url)
            tmdb = response.json()

            # Adiciona o filme à lista de dados
            tmdb_data.append(tmdb)
            
            # Marca o ID do filme como processado
            processed_ids.add(id_imdb)

            # Verifica se o arquivo JSON atual atingiu o limite de 100 registros ou se o tamanho excedeu 10 MB
            if len(tmdb_data) >= 100 or (len(json.dumps(tmdb_data, indent=4).encode('utf-8')) > 10 * 1024 * 1024):
                # Grava os dados acumulados no S3
                S3_CLIENT.put_object(Body=json.dumps(tmdb_data, indent=4), Bucket=BUCKET, Key=file_path)
                
                # Reseta a lista e incrementa o índice do arquivo
                tmdb_data = []
                file_index += 1
                file_path = f'Raw/TMDB/JSON/{current_date}/filmes_{file_index}.json'

        else:
            print(f"Nenhum resultado encontrado para o filme {id_imdb}.")
    
    # Grava quaisquer dados restantes que não foram gravados ainda
    if tmdb_data:
        S3_CLIENT.put_object(Body=json.dumps(tmdb_data, indent=4), Bucket=BUCKET, Key=file_path)
        
    return {'statusCode': 200, 'body': 'Processamento concluído e dados salvos no S3 com sucesso.'}
