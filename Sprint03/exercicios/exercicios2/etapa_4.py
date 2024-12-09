######################## ETAPA 4 ########################

# Abre e lê o arquivo 'actors.csv'
with open('actors.csv', 'r', encoding='utf-8') as file:
    conteudo = file.readlines()

# Remove a primeira linha do arquivo que contém o cabeçalho
cabecalho = conteudo.pop(0)

# Inicializa um dicionário para contar as aparições dos filmes
filmes_counter = {}

# Percorre todas as linhas do arquivo
for linha in conteudo:
    # Guarda os dados da linha separados por ',' e retira os espaços em branco
    dados = linha.strip().split(',')

    # Resolve o problema do nome do ator com aspas
    if len(dados) > 6:
        dados = [dados[0] + ',' + dados[1]] + dados[2:]

    # Pega o nome do filme de maior bilheteira em que o ator atuou
    filme = dados[4].strip()

    # Atualiza o contador com o nome do filme
    if filme in filmes_counter:
        filmes_counter[filme] += 1
    else:
        filmes_counter[filme] = 1

# Ordena os filmes pela quantidade de aparições e, em caso de empate, pelo nome do filme
filmes_ordenados = sorted(filmes_counter.items(), key=lambda x: (-x[1], x[0]))

# Armazena o resultado em 'etapa-4.txt'
with open('etapa-4.txt', 'w', encoding='utf-8') as file:
    for filme, quantidade in filmes_ordenados:
        file.write(f'O filme ({filme}) aparece {quantidade} vez(es) no dataset.\n')

# Mensagem de confirmação no console
print('Resultado da etapa 4 armazenado em etapa-4.txt.')
