# Análise de dados
# Concatena os elementos de uma lista de strings.
#
# Tipos de dados
#  Os elementos do tipo string estarão em uma lista. 

def concatenacao_elementos(lst: list[str]) -> str:
    '''
    Concatena as strings presentes em *lst*, desde que a lista não seja vazia.
    
    Exemplos
    >>> concatenacao_elementos(['giovana', ' me', ' devolve', ' o', ' gabriel'])
    'giovana me devolve o gabriel'
    >>> concatenacao_elementos(['Bom', ' dia', ' !'])
    'Bom dia !'
    '''
    concatenacao_elementos = ''
    for s in lst:
        concatenacao_elementos = concatenacao_elementos + s
    return concatenacao_elementos
    