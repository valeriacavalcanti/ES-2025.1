# ler um texto e exibir as vogais desse texto.

texto = input('Texto: ')
vogais = 'aeiouAEIOU'

for simbolo in texto:
    if simbolo in vogais:
        print(simbolo)
