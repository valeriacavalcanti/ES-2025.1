nota1, nota2, nota3 = input('Digite as 3 notas: ').split()
nota1, nota2, nota3 = int(nota1), int(nota2), int(nota3)

media = (nota1 + (nota2 + nota3)) / 3

print(nota1,nota2,nota3)
print()
print(media)

print()
print()

print(nota1, nota2, nota3, sep='/')

print('media =', media)
print('media = {media}')
print(f'media = {media:.2f}')


