arquivo = 'arquivo_texto.txt'

with open(arquivo, 'r') as file:
    linhas = file.readlines()

for linha in linhas:
    print(linha, end='') 