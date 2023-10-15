# Analise
# Conta quantas vezes um valor mínimo aparece em uma lista de inteiros não vazia.
# Tipos de dados
# A lista será composta de inteiros

def contagem_minimo(lst: list[int]) -> int:
    '''
    Conta quantas vezes o menor valor de *lst* aparece. *lst* não pode ser uma lista vazia.
    Exemplos
    >>> contagem_minimo([1,3,4,1])
    2
    >>> contagem_minimo([2,3,4,3])
    1
    >>> contagem_minimo([1])
    1
    '''
    minimo = lst[0]
    contagem = 0
    x = 0
    while x < len(lst):
        if lst[x] == minimo:
            contagem = contagem + 1
        if lst[x] < minimo:
            contagem = 1
            minimo = lst[x] 
        x = x + 1
    return contagem
    