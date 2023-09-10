# Analise
# Calcula o produto entre todos os elementos de uma lista de inteiros

# Tipos de dados
# A lista será composta de inteiros

def produto_lista(lst: list[int]) -> int:
    '''
    Calcula o produto entre todos os inteiros de *Lst*.
    Exemplos
    >>> produto_lista([1,3,4])
    12
    >>> produto_lista([0,1,2])
    0
    '''
    produto = lst[0]
    for x in lst:
        produto = produto * x
    return produto
