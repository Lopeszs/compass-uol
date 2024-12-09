numeros = [0]*3

for i in range (0,3):
    numeros[i] = i+1

for i in range (0,3):
    if(numeros[i] % 2 == 0):
        print('Par:', numeros[i])
    else:
        print('Ímpar:', numeros[i])