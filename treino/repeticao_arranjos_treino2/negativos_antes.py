# Analise
# Cria uma nova lista a partir de uma lista de inteiros, colocando os números negativos antes dos positivos.
# Tipos de dados
# A lista será composta de inteiros positivos.

def negativos_antes(lst: list[int]) -> list[int]:
    '''
    Cria uma nova lista a partir de *lst*, colocando os negativos antes dos positivos e do zero.
    Exemplos:
    >>> negativos_antes([0,2,3,-1,-2])
    [-1, -2, 0, 2, 3]
    >>> negativos_antes([0,2,3,4,5])
    [0, 2, 3, 4, 5]
    >>> negativos_antes([-2,-4,-5,-1,-2])
    [-2, -4, -5, -1, -2]
    '''
    positivos = []
    negativos = []
    i = 0
    while i < len(lst):
        if lst[i] < 0:
            negativos.append(lst[i])
        if lst[i] >= 0:
            positivos.append(lst[i])
        i = i + 1
    return negativos + positivos