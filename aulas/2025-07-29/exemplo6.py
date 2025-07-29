texto = 'eu amo ESTUDAR python em 2025 !!'

# numeros: 4
# simbolos minusculos: 13
# simbolos maiusculos: 7
# caracteres especiais: 8

qt_numeros = 0
qt_minusculos = 0
qt_maiusculos = 0
qt_especiais = 0

for s in texto:
    if s >= '0' and s <= '9':
        qt_numeros += 1
    elif s >= 'a' and s <= 'z':
        qt_minusculos += 1
    elif s >= 'A' and s <= 'Z':
        qt_maiusculos += 1
    else:
        qt_especiais += 1

print(qt_numeros)
print(qt_minusculos)
print(qt_maiusculos)
print(qt_especiais)
