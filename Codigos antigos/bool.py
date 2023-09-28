# Análise
# Verifica se todos os elementos de uma lista são falsos.

# Tipos de dados
# Os elementos da lista de booleanos serão do tipo bool.

def lista_bool(lst: list[bool]) -> bool:
    '''
    Verificar se todos os elementos de uma *lst* de booleanos, que não é vazia, possuem valor *False*.
    >>> lista_bool([True,True,True])
    False
    >>> lista_bool([False,False,False])
    True
    >>> lista_bool([True,False])
    False
    '''
    resposta = True
    for n in lst:
        if n == True:
            resposta = False
    return resposta