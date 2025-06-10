def gerar_matriz(linhas: int, colunas: int) -> list:
    matriz = []

    for i in range(linhas):
        matriz.append([0] * colunas)

    return matriz

    

# Main

valores = gerar_matriz(3, 3)

# ler os valores
for i in range(3):
    for j in range(3):
        valores[i][j] = int(input())

print(valores)

# exibir os elementos que estão na diagonal principal

#qtd = 0
#for _ in range(10_000_000):
    #print('Elementos da diagonal principal')
#    for i in range(3):
#        for j in range(3):
#            if i == j:
                #print(valores[i][j])
#                qtd += 1


qtd = 0
for _ in range(10_000_000):
    #print('Elementos da diagonal principal')
    for i in range(3):
    #    print(valores[i][i])
        qtd += 1





    
