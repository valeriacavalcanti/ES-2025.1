soma = 0
numeros = [0] * 10

# Ler e armazenar valores na lista
for i in range(4):
    numeros[i] = int(input('Número: '))
    soma = soma + numeros[i]

media = soma / 4

print(numeros)
print(f'{media = }')

# Exibir os valores armazenados na lista
for i in range(4):
    if numeros[i] > media:
        print(numeros[i])
