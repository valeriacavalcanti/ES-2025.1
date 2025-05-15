# programa para ler uma nota válida para o suap!

nota = int(input('Nota: '))

while nota < 0 or nota > 100:
    print('Nota inválida')
    nota = int(input('Nota: '))

print('Nota:', nota)
