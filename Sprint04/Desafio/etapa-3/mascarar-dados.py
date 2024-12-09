import hashlib

while True:
    # Recebe uma entrada string
    entrada = input("Digite um texto para gerar o hash ou '0' para terminar: ")
    
    # Se o usuário digitar 0 o loop termina
    if entrada == '0':
        print("Encerrando...")
        break
    
    # Gera o hash da entrada inserida
    texto_hash = hashlib.sha1(entrada.encode('utf-8', errors='ignore')).hexdigest()
    
    # Imprime o hash gerado
    print(f"Hash do texto inserido: {texto_hash}\n")