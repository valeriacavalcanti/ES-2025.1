# programa exibir os símbolos maiúsculos

cod_A = ord('A')
cod_Z = ord('Z')
for i in range(cod_A, cod_Z + 1):
    print(i, chr(i), bin(i))

print('-' * 10)
    
cod_a = ord('a')
cod_z = ord('z')
for i in range(cod_a, cod_z + 1):
    print(i, chr(i), bin(i))
