def conta_vogais(texto: str) -> int:
    vogais = 'aeiouAEIOU'
    vogais_string = filter(lambda char: char in vogais, texto)
    
    return len(list(vogais_string))

    