arq = open('teste.csv', 'r')

#lista = arq.read().splitlines()

for registro in arq.read().splitlines():
    print(type(registro), registro)

#print(lista)

arq.close()
