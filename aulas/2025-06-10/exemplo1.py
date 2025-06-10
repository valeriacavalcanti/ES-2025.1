# matriz 4 x 3
matriz1 = [[0,0,0], [0,0,0], [0,0,0], [0,0,0]]

# alterar todos os elementos da matriz1 para 1.

for i in range(len(matriz1)):
    for j in range(len(matriz1[i])):
        matriz1[i][j] = 1

print(matriz1)
