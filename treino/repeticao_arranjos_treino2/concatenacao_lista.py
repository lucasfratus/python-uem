# Analise
# Concatena todos os elementos de uma lista de strings.

# Tipos de dados
# A lista será composta de strings.

def concatena_lista_strings(lst: list[str]) -> str:
    '''
    Concatena todos os elementos de *lst*, devolvendo uma única string
    Exemplos:
    >>> concatena_lista_strings(['',''])
    ''
    >>> concatena_lista_strings(['Eu',''])
    'Eu'
    >>> concatena_lista_strings(['Eu','amo','sorvete'])
    'Euamosorvete'
    '''
    concatenacao = ''
    for x in lst:
        concatenacao = concatenacao + x
    return concatenacao
