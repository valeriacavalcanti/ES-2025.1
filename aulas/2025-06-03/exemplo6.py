"""
  Escreva um programa para ler 10 números que estão em um arquivo.
  Ao final, exiba os números do último até o primeiro.
"""

arq = open('valores.txt', 'r')
lista = arq.read().splitlines()

#for i in range(len(lista)):
#    lista[i] = int(lista[i])

lista = list(map(int, lista))

for i in range(len(lista)-1, -1, -1):
    print(lista[i])
