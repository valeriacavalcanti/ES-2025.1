def status_1v(idade: int) -> str:
    if idade <= 15:
        return "Não pode"

    if idade == 16 or idade == 17:
        return "Pode"

    if idade >= 18 and idade <= 70:
        return "Obrigatório"

    if idade > 70:
        return "Pode"


def status_2v(idade: int) -> str:
    if idade <= 15:
        return "Não pode"
    else:
        if idade <= 17:
            return "Pode"
        else:
            if idade <= 70:
                return "Obrigatório"
            else:
                return "Pode"

def status_3v(idade: int) -> str:
    if idade <= 15:
        return "Não pode"
    else:
        if idade <= 17 or idade > 70:
            return "Pode"
        else:
            return "Obrigatório"


def status_4v(idade: int) -> str:
    if idade <= 15:
        return "Não pode"
    elif idade <= 17 or idade > 70:
        return "Pode"
    else:
        return "Obrigatório"


# Teste

print(status_1v(15))   # Não Pode
print(status_1v(17))   # Pode
print(status_1v(18))   # Obrigatório
print(status_1v(30))   # Obrigatório
print(status_1v(70))   # Obrigatório
print(status_1v(90))   # Pode
