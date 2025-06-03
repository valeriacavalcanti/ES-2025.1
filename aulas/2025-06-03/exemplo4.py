"""
 Programa para ler VÁRIOS números. Ao final, exiba todos os números que foram digitados.
 O programa deverá encerrar quando for digitado 0 (zero).
"""

numeros = []
#qtd = 0

num = int(input('Número: '))
while num != 0:
    numeros.append(num)
#    qtd += 1
    num = int(input('Número: '))

print(numeros)

for i in range(len(numeros)):
    print(numeros[i])
