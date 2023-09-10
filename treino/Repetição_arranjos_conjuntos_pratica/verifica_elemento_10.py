# Analise
# Verifica se todos elementos de uma lista são menores que 10.

# Tipo de dados
# A lista será composta de números inteiros.

def verifica_10(lst: list[int]) -> bool:
    '''
    Produz True se todos os elementos de *lst* são menores que 10, caso contrário, produz False.
    Exemplos
    >>> verifica_10([1,4,5])
    True
    >>> verifica_10([11,1,3])
    False
    '''
    verificacao = True
    for n in lst:
        if n < 10:
            verificacao = True
        else:
            verificacao = False
    return verificacao