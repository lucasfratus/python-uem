# Analise
# Determina o sinal de um número, devolvendo -1 para números negativos, 1 para positivos e 0 para o número 0.

# Tipos de dados
# O número será um número inteiro.

def sinal(numero: int) -> int:
    '''
    Devolve -1 quando *numero* for negativo, 1 quando *numero* for positivo e 0 quando *numero* = 0
    Exemplos
    >>> sinal(-2)
    -1
    >>> sinal(0)
    0
    >>> sinal(10)
    1
    '''
    if numero > 0:
        sinal_numero = 1
    elif numero == 0:
        sinal_numero = 0
    else:
        sinal_numero = -1
    return sinal_numero
