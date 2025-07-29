# programa para converter um texto para maiúsculo

texto = input('Texto: ')
novo_texto = ''

for s in texto:
    if s >= 'a' and s <= 'z':
        # converter para maiúsculo
        codigo = ord(s) - 32
        novo_texto += chr(codigo)
    else:
        novo_texto += s

print(texto)
print(novo_texto)
