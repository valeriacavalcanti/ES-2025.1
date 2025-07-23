# Escreva um programa para armazenar os nomes dos torcedores de diferentes times.
# Serão informados 6 torcedores.

# Times: flamengo, botafogo, treze

clubes = {}
clubes['FLAMENGO'] = []
clubes['BOTAFOGO'] = []
clubes['TREZE'] = []

for i in range(6):
    nome = input('Nome: ')
    time = input('Time: ')

    clubes[time].append(nome)

print(clubes)
