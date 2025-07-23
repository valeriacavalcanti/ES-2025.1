import random

def menor_maior(lista: list) -> list:
    menor = lista[0]
    maior = lista[0]
    for i in range(1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
        if lista[i] > maior:
            maior = lista[i]
    return menor, maior

            
# main

# gerar 10 valores aleatórios
numeros = []
for i in range(10):
    num = random.randint(1, 10)
    numeros.append(num)

print(numeros)
misterio = menor_maior(numeros)
print(type(misterio), misterio)

# mistério é uma tupla