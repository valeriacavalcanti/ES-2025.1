idade = int(input('Idade: '))

while idade < 0:
    print('Idade inválida')
    idade = int(input('Idade: '))

print('Idade válida: ', idade)
