def media_aritmetica(n1:int, n2:int, n3:int) -> int:
    """
        Calcular a média aritmética entre 3 notas.
        parâmetros:
            nota1: int - primeira nota
            nota2: int - segunda nota
            nota3: int - terceira nota

        retorno:
            int - média calculada
    """
    print(type(n1), n1)
    soma = n1 + n2 + n3
    media = soma / 3
    return media

def media_ponderada(n1, n2, n3, p1 = 2, p2 = 3, p3 = 5):
    return (n1 * p1 + n2 * p2 + n3 * p3) / (p1 + p2 + p3)


def somar(n1:int, n2:int, n3:int) -> int:
    #global nota1
    #nota1 = 100
    #print(f'{nota1=}')
    return n1 + n2 + n3
