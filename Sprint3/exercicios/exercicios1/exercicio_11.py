import json
arquivo = 'person.json'

with open(arquivo, 'r') as file:
    arquivo_lido = json.load(file)

print(arquivo_lido)
