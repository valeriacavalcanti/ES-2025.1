soma = 0

qtd = int(input('Quantidade de números: '))

for i in range(qtd):
    num = int(input(f'Número {i + 1}: '))
    soma = soma + num

media = soma/qtd

print(soma, media)

