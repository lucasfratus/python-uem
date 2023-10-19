# Analise
# Remove o elemento de um certo indice de uma lista, modificando essa lista de inteiros.
# Tipos de dados
# A lista será composta de inteiros
# O indice será um inteiro.

def remove_indice(lst: list[int], indice: int):
    '''
    Remove o elemento da posição *indice* de *lst*, modificando *lst*
    *indice* precisa ser menor que o len de *lst*
    Exemplos:
    >>> lst = [7, 1, 8, 9]
    >>> remove_indice(lst, 2)
    >>> lst
    [7, 1, 9]
    >>> lst = [3, 1, 4, 5]
    >>> remove_indice(lst, 3)
    >>> lst
    [3, 1, 4]
    >>> lst = [3, 4, 2]
    >>> remove_indice(lst, 2)
    >>> lst
    [3, 4]
    '''
    assert indice < len(lst)
    i = 0
    j = len(lst) - 1
    while i < j:
        if i == indice:
            t = lst[i]
            lst[i] = lst[j]
            lst[j] = t
        i = i + 1

    lst.pop()


