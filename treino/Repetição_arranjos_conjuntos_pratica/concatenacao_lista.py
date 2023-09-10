# Analise
# Concatena os elementos de uma lista de strings

# Tipos de dados
# Os elementos da lista serão strings.

def concatena (lst: list[str]) -> str:
    '''
    Concatena todas as strings de *lst*.
    Exemplos
    >>> concatena('Pedra','Agua')
    'PedraAgua'
    >>> concatena('Hoje','')
    'Hoje'
    >>> concatena('','')
    '''
    soma = ''
    for x in lst:
        soma = soma + x
    return soma