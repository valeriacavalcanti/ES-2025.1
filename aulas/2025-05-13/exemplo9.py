qtd_erros = 0

while True:
    nota = int(input('Nota: '))

    if nota >= 0 and nota <= 100:
        break

    qtd_erros += 1
    print('Nota inválida')


print(nota)
print('erros:', qtd_erros)
