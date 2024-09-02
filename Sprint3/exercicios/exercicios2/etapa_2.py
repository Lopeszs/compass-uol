######################## ETAPA 2 ########################

# Reabre o arquivo para a segunda etapa
with open('actors.csv', 'r', encoding='utf-8') as file:
    conteudo = file.readlines()

# Remove a primeira linha do arquivo que contém o cabeçalho
cabecalho = conteudo.pop(0)

# Inicializa as variáveis para guardar a soma dos valores e o contador
soma = 0.0
cont = 0

# Percorre todas as linhas do arquivo
for linha in conteudo:
    # Guarda os dados da linha separados por ',' e retira os espaços em branco
    dados = linha.strip().split(',')

    # Resolve o problema do nome do ator com aspas
    if len(dados) > 6:
        dados = [dados[0] + ',' + dados[1]] + dados[2:]

    # Converte os valores da coluna gross em float e soma eles, incrementando o contador a cada valor lido
    try:
        gross = float(dados[-1].strip())
        soma += gross
        cont += 1
    except ValueError:
        print(f'Valor inválido: {dados[-1]}')

# Calcula a média dos valores somados
media = soma / cont

# Armazena o resultado em 'etapa-2.txt'
with open('etapa-2.txt', 'w', encoding='utf-8') as file:
    file.write(f'A média de receita de bilheteira bruta dos principais filmes é -> {media:.2f}\n')

# Mensagem de confirmação no console
print('Resultado da etapa 2 armazenado em etapa-2.txt.')
