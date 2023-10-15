# Analise
# Calcula o produto de todos os elementos de uma lista de inteiros
# Tipos de dados
# A lista será composta por inteiros

def produto_lista(lst: list[int]) -> int:
    '''
    Calcula o produto entre todos os elementos de *lst*.
    Exemplos:
    >>> produto_lista([1,2])
    2
    >>> produto_lista([3,4,5,6])
    360
    >>> produto_lista([0,2,4,6,8,10])
    0
    '''
    i = 0
    produto = 1
    while i < len(lst):
        produto = produto * lst[i]
        i = i + 1
    return produto