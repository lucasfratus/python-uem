# Analise
# Devolve uma nova lista a partir de uma lista de números inteiros, removendo um elemento da posição especificada.
#
# Tipos de dados
# A lista será composta de inteiros
# A posição especificada será um inteiro não negativo.
def remove_posicao(lst: list[int], posicao: int) -> list[int]:
    '''
    Devolve uma nova lista a partir de *lst*, removendo o elemento de indice *posicao*.
    Exemplos:
    >>> remove_posicao([1,2,3,5],1)
    [1, 3, 5]
    >>> remove_posicao([2,3,4],6)
    [2, 3, 4]
    >>> remove_posicao([2],0)
    []
    '''
    i = 0
    lista_elemento_removido = []
    while i < len(lst):
        if i != posicao:
            lista_elemento_removido.append(lst[i])
        i = i + 1
    return lista_elemento_removido