def extrato(registros: list, coluna: int) -> dict:
    frequencia = {}
    for i in range(1, len(registros)):
        servidor = registros[i].split(',')
        info = servidor[coluna]
        if info not in frequencia.keys():
            frequencia[info] = 1
        else:
            frequencia[info] += 1
    return frequencia


# registros, coluna, informacao

def servidores(registros: list, coluna: int, informacao: str) -> list:
    lista = []
    for i in range(1, len(registros)):
        servidor = registros[i].split(',')
        if servidor[coluna] == informacao:
            lista.append(servidor[1])
    return lista
            


## main

arq = open('servidores.csv', 'r')

registros = arq.read().splitlines()

arq.close()

print('Jornadas')
frequencia = extrato(registros, 3)
for k, v in frequencia.items():
    print(k, v)


#print('Cargos')
#frequencia = extrato(registros, 2)
#for k, v in frequencia.items():
#    print(k, v)

print(servidores(registros, 3, '30 HORAS SEMANAIS'))


