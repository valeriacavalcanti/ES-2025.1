# função: calcular a média
def calcular_media(n1: int, n2:int) -> int:
    media = (n1 + n2)/2
    return round(media)


def status(n1: int, n2: int) -> str:
    media = calcular_media(n1, n2)
    if media >= 70:
        return "Aprovado"
    else:
        if media >= 40:
            return "Final"
        else:
            return "Reprovado"


def status_frequencia(media: int, frequencia: int) -> str:
    if media >= 70 and frequencia >= 75:
        return "Aprovado"
    else:
        return "Reprovado"



# Teste

nota1, nota2 = 90, 50
print(calcular_media(nota1, nota2))         # 70
print(status(nota1, nota2))                 # Aprovado

nota1, nota2 = 50, 60
print(calcular_media(nota1, nota2))         # 55
print(status(nota1, nota2))                 # Final

nota1, nota2 = 75, 0
print(calcular_media(nota1, nota2))         # 38
print(status(nota1, nota2))                 # Reprovado

