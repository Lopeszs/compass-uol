#Etapa 2: LISTA COM O NOME DE 20 ANIMAIS

animais = ["Sapo", "Macaco", "Girafa", "Esquilo", "Elefante", 
           "Cavalo", "Cachorro", "Gato", "Anta", "Golfinho", "Vaca",
           "Galinha", "Porco", "Touro", "Zebra", "Canguru",
           "Ovelha", "Alce", "Urso", "Raposa"]

animais.sort()

[print(animal) for animal in animais]

with open("animais.csv", "w") as arquivo:
    for animal in animais:
        arquivo.write(f"{animal}\n")    
