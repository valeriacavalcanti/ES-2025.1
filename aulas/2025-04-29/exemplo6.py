def quantidade_parcelas(valor: float) -> int:
    if valor <= 100:
        parcelas = 1
    elif valor <= 200:
        parcelas = 2
    elif valor <= 400:
        parcelas = 3
    elif valor <= 800:
        parcelas = 4
    else:
        parcelas = 5

    return parcelas


def valor_da_parcela(valor_compra: float) -> float:
    return valor_compra / quantidade_parcelas(valor_compra)


# Teste

print(valor_da_parcela(99))        # 99
print(valor_da_parcela(120))       # 60
print(valor_da_parcela(300))       # 100
print(valor_da_parcela(600))       # 150
print(valor_da_parcela(1000.20))   # 200.04
