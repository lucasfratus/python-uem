# Analise
# Coloca os elementos negativos de uma lista de inteiros antes dos negativos.
# Tipos de dados
# A lista será composta de números inteiros.

def negativos_antes(lst: list[int]):
    '''
    Coloca os elementos negativos antes dos não negativos de *lst*.
    *lst* não pode ser uma lista vazia
    Exemplos:
    >>> lst = [0,1]
    >>> negativos_antes(lst)
    >>> lst
    [0, 1]
    >>> lst = [-1,2,-2]
    >>> negativos_antes(lst)
    >>> lst
    [-1, -2, 2]
    >>> lst = [-1,-2,-3]
    >>> negativos_antes(lst)
    >>> lst
    [-1, -2, -3]
    '''
    i = 0
    while i < len(lst):
        if lst[i - 1] >= 0 and lst[i] < 0:
            t = lst[i]
            lst[i] = lst[i-1]
            lst[i-1] = t
        i = i + 1

