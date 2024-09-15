######################## ETAPA 1 ########################

# Código para encontrar o ator/atriz com o maior número de filmes
with open('actors.csv', 'r', encoding='utf-8') as file:
    conteudo = file.readlines()

# Remove a primeira linha do arquivo que contém o cabeçalho
cabecalho = conteudo.pop(0)

# Inicializa as variáveis para guardar o número de filmes e o nome do ator
filmes = 0
ator_filmes = ''

# Percorre todas as linhas do arquivo
for linha in conteudo:
    # Guarda os dados da linha separados por ',' e retira os espaços em branco
    dados = linha.strip().split(',')

    # Resolve o problema do nome do ator com aspas
    if len(dados) > 6:
        dados = [dados[0] + ',' + dados[1]] + dados[2:]

    # Pega o nome do ator e o número de filmes
    ator = dados[0].strip('"')
    
    # Remove os espaços em branco e converte para inteiro o número de filmes
    try:
        num_filmes = int(dados[2].strip()) 
    except ValueError:
        print(f'Valor inválido: {dados[2]}')
        continue

    # Verifica se o ator tem mais filmes que o ator guardado
    if num_filmes > filmes:
        filmes = num_filmes
        ator_filmes = ator

# Armazena o resultado em 'etapa-1.txt'
with open('etapa-1.txt', 'w', encoding='utf-8') as file:
    file.write(f'O ator/atriz com maior número de filmes é {ator_filmes} -> {filmes} filmes.\n')

# Mensagem de confirmação no console
print('Resultado da etapa 1 armazenado em etapa-1.txt.')