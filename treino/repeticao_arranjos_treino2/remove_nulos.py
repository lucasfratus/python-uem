# Analise
# Cria uma nova lista removendo todos os valores nulos de uma lista de inteiros.

# Tipos de dados
# A lista será composta de inteiros

def remove_nulos(lst: list[int]) -> list[int]:
    '''
    Cria uma nova lista a partir de *lst*, removendo todos os valores nulos.
    Exemplos:
    >>> remove_nulos([])
    []
    >>> remove_nulos([1,2,3])
    [1, 2, 3]
    >>> remove_nulos([1,0,5,7])
    [1, 5, 7]
    >>> remove_nulos([1,0,2,0,7])
    [1, 2, 7]
    '''
    i = 0
    nova_lista = []
    while i < len(lst):
        if lst[i] != 0:
            nova_lista.append(lst[i])
        i = i + 1
    return nova_lista