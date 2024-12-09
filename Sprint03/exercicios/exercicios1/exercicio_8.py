a = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto'] 

for i in range(6):
    if a[i] == a[i][::-1]:
        print('A palavra: '+ a[i] +' é um palíndromo')
    else:
        print('A palavra: '+ a[i] +' não é um palíndromo')