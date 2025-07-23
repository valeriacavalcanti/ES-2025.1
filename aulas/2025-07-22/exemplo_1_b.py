# programa para gerar 10 valores aleatórios entre 1 e 10, inclusive.
# Exibir os diferentes números gerados, desconsiderando as repetições e suas respectivas frequências.

import random

frequencia = {}

numeros = []
for i in range(10):
    num = random.randint(1, 10)
    numeros.append(num)

for elem in numeros:
    if elem in frequencia.keys():
        frequencia[elem] += 1
    else:
        frequencia[elem] = 1

print(numeros)
print(frequencia)

print('Valores e frequência - ordenado')
for chave in sorted(frequencia.keys()):
    print(chave, frequencia[chave])

print('\nValores e frequência - original')
for k, v in frequencia.items():
    print(k, v)
