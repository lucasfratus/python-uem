# Analise
# Verifica se algum dos elementos de uma lista de booleanos é verdadeiro.
# Tipos de dados
# A lista será composta de booleanos

def verifica_algum_verdadeiro(lst: list[bool]) -> bool:
    '''
    Produz True se algum elemento de *lst* é verdadeiro. Caso contrário, produz False.
    *lst* não pode ser vazia.
    Exemplos:
    >>> verifica_algum_verdadeiro([False,False,True])
    True
    >>> verifica_algum_verdadeiro([False,False])
    False
    >>> verifica_algum_verdadeiro([True,True])
    True
    '''
    i = 0
    verificacao = False
    while i < len(lst) and verificacao == False:
        if lst[i] == True:
            verificacao = True
        i = i + 1
    return verificacao