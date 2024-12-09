######################## ETAPA 3 ########################

# Abre e lê o arquivo 'actors.csv'
with open('actors.csv', 'r', encoding='utf-8') as file:
    conteudo = file.readlines()

# Remove a primeira linha do arquivo que contém o cabeçalho
cabecalho = conteudo.pop(0)

# Inicializa as variáveis para guardar o ator com a maior média e o valor da maior média
maior_media = 0.0
ator_media = ''

# Percorre todas as linhas do arquivo
for linha in conteudo:
    # Guarda os dados da linha separados por ',' e retira os espaços em branco
    dados = linha.strip().split(',')
    
    # Resolve o problema do nome do ator com aspas
    if len(dados) > 6:
        dados = [dados[0] + ',' + dados[1]] + dados[2:]

    # Guarda a maior media por filme e o nome do ator com a maior media
    try:
        media_por_filme = float(dados[3].strip()) 
        if media_por_filme > maior_media:  
            maior_media = media_por_filme
            ator_media = dados[0].strip() 
    except ValueError:
        print(f'Valor invalido: {dados[3]}')

# Armazena o resultado em 'etapa-3.txt'
with open('etapa-3.txt', 'w', encoding='utf-8') as file:
    file.write(f'O ator/atriz com a maior média de receita de bilheteria bruta por filme é {ator_media} -> US${maior_media:.2f}.')

# Mensagem de confirmação no console
print('Resultado da etapa 3 armazenado em etapa-3.txt.')
