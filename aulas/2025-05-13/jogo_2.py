import random

menor = 1
maior = 100

numero_secreto = random.randint(menor, maior)
print(numero_secreto)

while True:
    chute = int(input(f'Chute (entre {menor} e {maior}): '))

    if (chute == numero_secreto):
        break
    
    print('Não acertou')

    if chute > numero_secreto:
        maior = chute
    else:
        menor = chute

    if (menor + 1 == maior - 1):
        break
        

if chute == numero_secreto:
    print('Ganhou')
else:
    print('Perdeu')
    
print(chute, numero_secreto)
    
