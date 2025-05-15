while True:
    nota = int(input('Nota: '))

    if nota >= 0 and nota <= 100:
        break
    
    print('Nota inválida')
    
print('Nota:', nota)
