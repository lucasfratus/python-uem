# Análise
# Realiza o produto dos elementos da lista.

# Tipos de dados
# Os elementos da lista serão números inteiros
def produto_lista(lst: list[int]) -> int:
    '''
    Calcular o produto de todos os elementos da *lst*, exceto se for vazia.
    Exemplos
    >>> produto_lista([50,10])
    500
    >>> produto_lista([0,5])
    0
    >>> produto_lista([100,-2])
    -200
    '''
    produto_lista = 1
    for s in lst:
        produto_lista = produto_lista * s
    return produto_lista