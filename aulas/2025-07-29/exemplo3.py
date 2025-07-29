# ler um texto e exibir os diferentes símbolos digitados com respectivas frequências.

texto = input('Texto: ')
frequencia = {}

for simbolo in texto:
    if simbolo not in frequencia:
        frequencia[simbolo] = 1
    else:
        frequencia[simbolo] += 1

for chave, valor in frequencia.items():
    print(chave, valor)
