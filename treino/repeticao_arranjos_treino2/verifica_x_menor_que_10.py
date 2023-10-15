# Analise
# Verifica se todos os elementos de uma lista de inteiros são menores que 10.
# Tipos de dados
# A lista será composta de números inteiros.

def verifica_x_menor_10(lst: list[int]) -> bool:
    '''
    Produz True se todos os elementos de *lst* forem menores que 10. Caso contrário, produz False.
    Exemplos:
    >>> verifica_x_menor_10([])
    True
    >>> verifica_x_menor_10([5,7,8,1,9])
    True
    >>> verifica_x_menor_10([10])
    False
    >>> verifica_x_menor_10([133,8,7,5])
    False
    '''
    i = 0
    menor_10 = True
    while i < len(lst) and menor_10:
        if lst[i] >= 10:
            menor_10 = False
        i = i + 1
    return menor_10