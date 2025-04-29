# Escreva um programa para ler os 3 lados de um triângulo, informe o tipo de triângulo formado.
def tipo_triangulo(lado1: int, lado2: int, lado3: int) -> str:
    if lado1 == lado2 and lado1 == lado3:
        return 'Equilátero'
    else:
        if lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
            return 'Escaleno'
        else:
            return 'Isósceles'

def maior_lado(lado1: int, lado2: int, lado3: int) -> int:
    if lado1 > lado2 and lado1 > lado3:
        return lado1
    else:
        if lado2 > lado3:
            return lado2
        else:
            return lado3

def verificar_forma_triangulo(lado1: int, lado2: int, lado3: int) -> bool:
    maior = maior_lado(lado1, lado2, lado3)
    soma_dos_outros_lados = lado1 + lado2 + lado3 - maior
    if soma_dos_outros_lados > maior:
        return True
    else:
        return False


# Teste

'''
print(tipo_triangulo(1,1,1))  # equilátero
print(tipo_triangulo(1,1,2))  # isósceles
print(tipo_triangulo(1,2,1))  # isósceles
print(tipo_triangulo(2,1,1))  # isósceles
print(tipo_triangulo(1,2,3))  # escaleno

print(maior_lado(5, 10, 9))     # 10
print(maior_lado(15, 10, 9))    # 15
print(maior_lado(5, 10, 90))    # 90
print(maior_lado(5, 5, 5))      # 5

print(verifica_forma_triangulo(5, 3, 4))    # True
print(verifica_forma_triangulo(5, 2, 1))    # False
print(verifica_forma_triangulo(5, 5, 5))    # True
'''


# Main

l1, l2, l3 = input("Três lados: ").split()
l1, l2, l3 = int(l1), int(l2), int(l3)

if verificar_forma_triangulo(l1, l2, l3) == True:
    print(tipo_triangulo(l1, l2, l3))
else:
    print('Não forma triângulo')


    
    
