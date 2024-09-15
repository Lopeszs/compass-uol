def maiores_que_media(conteudo: dict) -> list:
    precos = list(conteudo.values())
    media = sum(precos) / len(precos)
    
    acima_media = [(nome, preco) for nome, preco in conteudo.items() if preco > media]
    
    acima_media.sort(key=lambda x: x[1])
    
    return acima_media
