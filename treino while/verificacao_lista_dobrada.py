# Analise
# Verifica se uma lista de números inteiros é dobrada, ou seja, pode ser obtida através da concatenação de listas iguais.
#
# Tipos de dados
# A lista será composta por números inteiros

def verifica_lista_dobrada(lst: list[int]) -> bool:
    '''
    Produz True caso *lst* seja dobrada, ou seja, pode ser obtida através da concatenação de duas listas iguais. Caso contrário,
    produz False.
    Exemplos:
    >>> verifica_lista_dobrada([])
    True
    >>> verifica_lista_dobrada([1,2,3,1,2,3])
    True
    >>> verifica_lista_dobrada([0,1,2,5,7])
    False
    >>> verifica_lista_dobrada([1,2,3,1,2,3,4])
    False
    '''
    verificacao = True
    if len(lst) > 2:
        # Começa do meio de *lst*
        i = 0
        j = lst[int(len(lst)/2) - 1]
        while j < len(lst):
            if lst[i] != lst[j]:
                verificacao = False
            i = i + 1
            j = j + 1
    return verificacao


