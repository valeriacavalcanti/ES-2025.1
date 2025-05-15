nota = int(input('Nota: '))
qtd_erros = 0

while nota < 0 or nota > 100:
    qtd_erros += 1
    
    print('Nota inválida')
    
    nota = int(input('Nota: '))


print(nota)
print('erros:', qtd_erros)
