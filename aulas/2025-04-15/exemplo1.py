import funcoes


## PROGRAMA PRINCIPAL


# obter as 3 notas
nota1 = float(input('Nota 1: '))
nota2 = int(input('Nota 2: '))
nota3 = int(input('Nota 3: '))

# calcular a média aritmetica
ma = funcoes.media_aritmetica(nota1, nota2, nota3)

# calcular a média ponderada (2, 3 e 5)
mp = funcoes.media_ponderada(nota1, nota2, nota3, 4, 7, 9)

# exibir as duas médias
print(ma)
print(mp)
