def gerar_matriz(linhas: int, colunas: int) -> list:
    matriz = []

    for i in range(linhas):
        matriz.append([0] * colunas)

    return matriz


def media_geral(matriz: list) -> float:
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma += matriz[i][j]
    qtd = len(matriz) * len(matriz[0])
    return soma / qtd
    

# Main

# alunos: 4, avaliacao: 3

notas = gerar_matriz(4, 3)


# ler as notas de todos os alunos

for i in range(4): # alunos
    for j in range(3): # notas
        #notas[i][j] = int(input(f'Aluno {i + 1} Nota {j + 1}: '))
        notas[i][j] = int(input())


# exibir as notas
print(notas)


# exibir a média de cada aluno

for i in range(4):
    soma = 0
    for j in range(3):
        soma += notas[i][j]
    media = soma / 3
    print(f'Aluno {i + 1} - Média {media}')


# exibir a média de cada avaliação

for j in range(3):
    soma = 0
    for i in range(4):
        soma += notas[i][j]
    media = soma / 4
    print(f'Avaliação {j + 1} - Média {media}')


# exibir a média geral
print(f'Média da turma: {media_geral(notas)}')

