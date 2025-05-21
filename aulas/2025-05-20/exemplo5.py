soma_media = 0
soma_aluno = 0
qtd_alunos = 0

for i in range(3):
    soma = 0
    #print('turma', i)
    qtd = int(input('Quantidade de alunos: '))
    qtd_alunos += qtd
    for j in range(qtd):
        #print('aluno', j)
        nota = int(input(f'Turma {i} Aluno {j}: '))
        soma_aluno += nota
        soma += nota
    media = soma / qtd
    soma_media += media
    print(f'{media=}')

media_geral_turma = soma_media/3
media_geral_aluno = soma_aluno/qtd_alunos

print(f'{media_geral_turma = }')
print(f'{media_geral_aluno = }')
