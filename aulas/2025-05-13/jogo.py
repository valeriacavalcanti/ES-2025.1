import random

menor = 1
maior = 100

numero_secreto = random.randint(menor, maior)
print(numero_secreto)

chute = int(input(f'Chute (entre {menor} e {maior}): '))

while chute != numero_secreto:
    print('Não acertou')

    if chute > numero_secreto:
        maior = chute
    else:
        menor = chute

    if (menor + 1 == maior - 1):
        break
        
    chute = int(input(f'Chute (entre {menor} e {maior}): '))


if chute == numero_secreto:
    print('Ganhou')
else:
    print('Perdeu')
    
print(chute, numero_secreto)
    
