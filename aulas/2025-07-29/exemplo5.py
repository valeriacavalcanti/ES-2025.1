# ler um texto e exibir as consoantes desse texto.

texto = input('Texto: ')
vogais = 'aeiouAEIOU'

for simbolo in texto:
    if simbolo not in vogais:
        print(simbolo)
