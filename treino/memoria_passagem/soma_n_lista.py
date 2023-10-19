# Analise
# Soma um valor especificado em cada elemento de uma lista de inteiros.

# Tipos de dados
# A lista será composta por inteiros
# O valor especificado será um inteiro

def soma_n_lista(lst: list[int], n: int) -> list[int]:
    '''
    Soma *n* em todos os elementos de *lst*.
    Exemplos:
    >>> x = [1, 2, 3]
    >>> soma_n_lista(x, 1)
    >>> x
    [2, 3, 4]
    >>> x = [1,2,3]
    >>> soma_n_lista(x,0)
    >>> x
    [1, 2, 3]
    >>> x = [2, 4, 7]
    >>> soma_n_lista(x,-2)
    >>> x
    [0, 2, 5]
    '''
    i = 0
    while i < len(lst):
        t = lst[i] + n
        lst[i] = t
        i = i + 1