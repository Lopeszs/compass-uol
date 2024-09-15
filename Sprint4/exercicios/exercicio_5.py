import csv

def processar_notas(caminho_csv):
    with open(caminho_csv, mode='r') as file:
        reader = csv.reader(file)
        
        estudantes = []
        for linha in reader:
            nome = linha[0]
            notas = list(map(float, linha[1:]))
            
            tres_maiores_notas = sorted(notas, reverse=True)[:3]
            
            media_tres_maiores = sum(tres_maiores_notas) / 3
            
            estudantes.append((nome, tres_maiores_notas, media_tres_maiores))
        
        estudantes.sort(key=lambda x: x[0])
        
        for estudante in estudantes:
            nome, notas, media = estudante
            notas_inteiras = [int(nota) for nota in notas]
        
            media_arredondada = round(media, 2)
            if media_arredondada.is_integer():
                media_formatada = f"{round(media, 1):.1f}"
            else:
                media_formatada = f"{media_arredondada:.2f}"
            
            print(f"Nome: {nome} Notas: {notas_inteiras} Média: {media_formatada}")

processar_notas('estudantes.csv')
