# Etapa 1: LISTA COM 250 INTEIROS ALEATÓRIOS

import random

inteiros = [0] * 250

for i in range(250):
    inteiros[i] = random.randint(1, 10000)

inteiros.reverse()
print(inteiros)
