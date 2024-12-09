def tres(lista):
    tam = len(lista) // 3
    lista1 = lista[:tam]
    lista2 = lista[tam:2*tam]
    lista3 = lista[2*tam:]
    return lista1, lista2, lista3

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

result = tres(lista)

print(result[0], result[1], result[2])