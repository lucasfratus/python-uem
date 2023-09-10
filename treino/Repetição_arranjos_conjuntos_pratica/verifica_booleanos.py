# Analise
# Verifica se todos os elementos de uma lista de booleanos são falsos.

# Tipos de dados
# A lista será compostas de booleanos.

def verifica_booleanos(lst: list[bool]) -> bool:
    '''
    Produz True se todos os elementos de *lst* forem False, caso contrário produz False.
    Exemplo
    >>> verifica_booleanos([True,False,False])
    False
    >>> verifica_booleanos([False,False,False])
    True
    '''
    verifica = True
    for n in lst:
        if n == True:
            verifica = False
    return verifica