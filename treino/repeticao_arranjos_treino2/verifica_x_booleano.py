# Analise
# Verifica se todos os elementos de uma lista de booleanos são falsos.
# Tipos de dados
# A lista é composta de booleanos

def verifica_x_falso(lst: list[bool]) -> bool:
    '''
    Produz True se todos os elementos de *lst* são falsos. Caso contrário, produz False.
    *lst* não deve ser uma lista vazia
    Exemplos:
    >>> verifica_x_falso([False,False])
    True
    >>> verifica_x_falso([False,True])
    False
    >>> verifica_x_falso([True,True,True])
    False
    '''
    i = 0
    verificacao = True
    while i < len(lst) and verificacao:
        if lst[i] == True:
            verificacao = False
        i = i + 1
    return verificacao
