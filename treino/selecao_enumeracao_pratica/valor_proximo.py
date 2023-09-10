# Analise
# Determina o valor entre 0 a 100 mais próximo de um dado numero inteiro.

# Tipos de dados
# O número será um inteiro

def valor_proximo(numero_dado: int) -> int:
    '''
    Determina qual valor entre 0 e 100 é mais próximo de *numero_dado*.
    >>> valor_proximo(14)
    14
    >>> valor_proximo(-1)
    0
    >>> valor_proximo(106)
    100
    '''
    if numero_dado >= 0 and numero_dado <= 100:
        valor_proximo = numero_dado
    elif numero_dado > 100:
        valor_proximo = 100
    else:
        valor_proximo = 0
    return valor_proximo