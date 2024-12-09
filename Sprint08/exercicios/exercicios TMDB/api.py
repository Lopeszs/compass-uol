import requests
import pandas as pd
from IPython.display import display
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

# URL para filmes em cartaz
url = f"https://api.themoviedb.org/3/movie/now_playing?api_key={api_key}&language=pt-BR"

# Fazendo a requisição para a API
response = requests.get(url)

data = response.json()
filmes = []

    # Extraindo os dados de cada filme
for movie in data['results']:
    filme_info = {
        'Titulo': movie['title'],
        'Data de Lancamento': movie['release_date'],
        'Visão Geral': movie['overview'],
        'Votos': movie['vote_count'],
        'Média de Votos': movie['vote_average']
    }
    filmes.append(filme_info)

# Criando o DataFrame
df = pd.DataFrame(filmes)
display(df)








