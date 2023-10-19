# Analise
# Encontra o valor máximo de uma lista de inteiros não vazia.
#
# Tipos de dados
# A lista será composta de inteiros.

def encontra_max(lst: list[int], i: int, maximo = int) -> int:
    '''
    Encontra o valor inteiro máximo de *lst*. *lst* não pode ser um lista vazia.
    *i* deve ser 0
    Exemplos:
    >>> encontra_max([1,2,3,4],0,0)
    4
    >>> encontra_max([-1,0,-2],0,0)
    0
    >>> encontra_max([1],0,0)
    1
    '''
    if i == len(lst):
        maximo = lst[i-1]
    else:
        if lst[i] >= maximo:
            maximo = lst[i]
            maximo = encontra_max(lst,i+1,maximo)
    return maximo
    