def my_map(lista, f):
    for i in range(len(lista)):
        lista[i] = f(lista[i])
    return lista

def f(num):
    return num ** 2

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(my_map(lista, f))