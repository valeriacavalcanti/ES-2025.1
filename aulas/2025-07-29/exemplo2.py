# ler um texto e exibir os diferentes símbolos digitados

texto = input('Texto: ')
distintos = []

for s in texto:
    if s not in distintos:
        distintos.append(s)

print(distintos)
