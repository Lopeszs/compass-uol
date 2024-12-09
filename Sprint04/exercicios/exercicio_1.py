def processar_numeros_arquivo(arquivo: str):
    with open(arquivo, 'r') as file:
        numeros = list(map(int, file.readlines()))
    
    pares = list(filter(lambda x: x % 2 == 0, numeros))

    maiores_pares = sorted(pares, reverse=True)[:5]
    
    soma_maiores_pares = sum(maiores_pares)
    
    print(maiores_pares)
    print(soma_maiores_pares)

processar_numeros_arquivo('number.txt')
