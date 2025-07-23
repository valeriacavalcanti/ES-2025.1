# programa para gerar 100 valores aleatórios entre 1 e 50, inclusive.
# Exibir os diferentes números gerados, desconsiderando as repetições.

import random

def diferentes(lista: list) -> tuple:
    temp = []

    for elem in lista:
        if elem not in temp:
            temp.append(elem)
    return tuple(temp)


## Main

numeros = []
for i in range(100):
    num = random.randint(1, 50)
    numeros.append(num)

distintos = diferentes(numeros)
print(numeros)
print(type(distintos), distintos)
