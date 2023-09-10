# Analise
# Devolve uma lista de inteiros sem os valores negativos da lista original.

# Tipos de dados
# A lista será composta de naturais(inteiros positivos)

def remover_negativos(lst: list[int]) -> list[int]:
    '''
    Remove os valores negativos de *lst*, devolvendo uma nova lista apenas com valores nulos e positivos.
    Exemplos
    >>> remover_negativos([-1,1,2,3])
    [1,2,3]
    >>> remover_negativos([-3,0])
    [0]
    >>> remover_negativos([0])
    [0]
    >>> remover_negativos([])
    []
    '''
    lista_sem_negativos = []
    for x in lst:
        if x >= 0:
            lista_sem_negativos.append(x)
    return lista_sem_negativos
