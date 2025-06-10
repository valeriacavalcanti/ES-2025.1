idades = [0] * 6
nomes = [''] * 6
soma = 0

for i in range(6):
    nomes[i] = input('Nome: ')
    idades[i] = int(input('Idade: '))
    soma += idades[i]

menor = maior = idades[0]

media = soma / 6

# exibir o nome e a idade de cada pessoa
for i in range(6):
    if idades[i] > media:
        print(f'{nomes[i]} {idades[i]}')
    if idades[i] > maior:
        maior = idades[i]
    if idades[i] < menor:
        menor = idades[i]

# vamos descobrir quem tem a maior e a menor idade
for i in range(6):
    if idades[i] == maior:
        print('Maior: ', nomes[i])
    if idades[i] == menor:
        print('Menor: ', nomes[i])
