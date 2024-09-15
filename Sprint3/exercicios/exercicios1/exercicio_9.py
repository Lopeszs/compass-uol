primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for i, nome in enumerate(primeirosNomes):
    sobreNome = sobreNomes[i]
    idade = idades[i]
    print(f'{i} - {nome} {sobreNome} está com {idade} anos')