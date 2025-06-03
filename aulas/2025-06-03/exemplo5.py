"""
 Programa para ler 8 números. Ao final, exiba o maior valor digitado.
 Ao final:
 - Exibir todos os números digitados.
 - Exibir quantas vezes foram digitados valores iguais ao último número lido.
"""

def maior_valor(lista: list) -> int:
    maior = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > maior:
            maior = lista[i]
    return maior


def menor_valor(lista: list) -> int:
    menor = lista[0]
    for i in range(1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
    return menor


def somar(lista: list) -> int:
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    return soma


def printv(lista: list):
    for i in range(len(lista)):
        print(lista[i])


def quantidade(lista: list, numero: int) -> int:
    qtd = 0
    for i in range(len(lista)):
        if lista[i] == numero:
            qtd += 1
    return qtd


# Main

qtd = int(input('Quantidade de números: '))
numeros = [0] * qtd

# ler os números
for i in range(qtd):
    numeros[i] = int(input('Número: '))

printv(numeros)
print(somar(numeros), sum(numeros))
print(menor_valor(numeros), min(numeros))
print(maior_valor(numeros), max(numeros))
print(quantidade(numeros, 40), numeros.count(40))
