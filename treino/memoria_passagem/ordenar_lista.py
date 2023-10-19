# Análise
# Ordena um lista de números inteiros de forma crescente.

# Tipos de dados
# A lista será composta de números inteiros.

def ordenar(lst: list[int]):
    '''
    Ordena *lst* de forma crescente.
    *lst* não pode ser uma lista vazia
    Exemplos:
    >>> lst = [1,2,3,4]
    >>> ordenar(lst)
    >>> lst
    [1, 2, 3, 4]
    >>> lst = [1,3,2,4,5,6]
    >>> ordenar(lst)
    >>> lst
    [1, 2, 3, 4, 5, 6]
    >>> lst  = [6,5,4,3,2,1]
    >>> ordenar(lst)
    >>> lst
    [1, 2, 3, 4, 5, 6]
    >>> lst  = [-6,5,4,3,2,1]
    >>> ordenar(lst)
    >>> lst
    [-6, 1, 2, 3, 4, 5]
    '''
    for x in range(len(lst)):
        menor = x
        for y in range(x+1, len(lst)):
            if lst[y] < lst[menor]:
                menor = y
        elemento = lst[x]
        lst[x] = lst[menor]
        lst[menor] = elemento
        

                
