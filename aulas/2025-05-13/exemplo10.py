# + - * / s

valor1 = int(input('Valor 1: '))
valor2 = int(input('Valor 2: '))

operador = input('Operador: ')

while operador != 's' and operador != 'S':
    if operador == '+':
        print(valor1 + valor2)
    elif operador == '-':
        print(valor1 - valor2)
    elif operador == '*':
        print(valor1 * valor2)
    elif operador == '/':
        if valor2 != 0:
            print(valor1 / valor2)
        else:
            print('divisao por zero')
    else:
        print('operador inválido')

    operador = input('Operador: ')

print('terminou')
