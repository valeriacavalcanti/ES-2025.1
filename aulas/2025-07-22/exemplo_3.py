# programa para ler e armazenar os dados (nome, idade e cpf) de 3 pessoas.

pessoas = []

for i in range(3):
    pessoa = {}
    pessoa['nome'] = input('Nome: ')
    pessoa['idade'] = int(input('Idade: '))
    pessoa['cpf'] = input('Cpf: ')
    
    pessoas.append(pessoa)

for i in range(3):
    print(pessoas[i]['nome'], pessoas[i]['idade'], pessoas[i]['cpf'])
