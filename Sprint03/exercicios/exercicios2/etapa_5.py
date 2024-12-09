######################## ETAPA 5 ########################

# Abre e lê o arquivo 'actors.csv'
with open('actors.csv', 'r', encoding='utf-8') as file:
    conteudo = file.readlines()

# Remove a primeira linha do arquivo que contém o cabeçalho
cabecalho = conteudo.pop(0)

# Cria um dicionário para armazenar a receita bruta total de cada ator
atores_receita = {}

# Percorre todas as linhas do arquivo
for linha in conteudo:
    # Guarda os dados da linha separados por ',' e retira os espaços em branco
    dados = linha.strip().split(',')
    
    # Resolve o problema do nome do ator com aspas
    if len(dados) > 6:
        dados = [dados[0] + ',' + dados[1]] + dados[2:]

    # Pega o nome do ator e a receita bruta total
    ator = dados[0].strip('"')
    
    try:
        total_bruto = float(dados[1].strip())
        # Armazena a receita bruta total no dicionário
        atores_receita[ator] = total_bruto
    except ValueError:
        print(f'Valor inválido: {dados[1]}')

# Ordena os atores pela receita bruta total, em ordem decrescente
atores_ordenados = sorted(atores_receita.items(), key=lambda x: x[1], reverse=True)

# Armazena o resultado em 'etapa-5.txt'
with open('etapa-5.txt', 'w', encoding='utf-8') as file:
    for ator, receita in atores_ordenados:
        file.write(f'{ator} - {receita:.2f}\n')

# Mensagem de confirmação no console
print('Resultado da etapa 5 armazenado em etapa-5.txt.')