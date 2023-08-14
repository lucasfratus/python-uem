def sinal(numero:float ) -> int:
    '''
    Determina um sinal a um numero, levando em conta se o numero e' positivo, negativo ou zero.
    Exemplos
    >>> sinal(10)
    +1
    >>> sinal(-2)
    -1
    >>> sinal(0)
    0
    '''
    if numero > 0:
        numero = +1
    elif numero == 0:
        numero = 0
    else:
        numero = -1
    return numero
    