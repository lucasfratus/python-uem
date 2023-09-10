# Analise
# Cria uma lista removendo todos os elementos nulos(0) de uma lista de números inteiros.

# Tipos de dados
# A lista será composta de números inteiros.

def remover_nulos(lst: list[int]) -> list[int]:
    '''
    Cria uma lista removendo todos os 0 de *lst*. *lst* nao pode ser vazia.
    Exemplos
    >>> remover_nulos([1,1,0,3])
    [1,1,3]
    >>> remover_nulos([1,1,3,4])
    [1,1,3,4]
    '''
    lista = []
    for n in lst:
        if n != 0:
            lista.append(n)
    return lista
        