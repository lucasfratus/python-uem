# Analise
# Concatena todas as strings de uma lista de strings
# Tipos de dados
# A lista será composta de strings

def concatena_strings(lst: list[str],x: int) -> str:
    '''
    Concatena todas as strings de *lst*, sendo *x* igual a 0
    Exemplos:
    >>> concatena_strings([],0)
    ''
    >>> concatena_strings(['','a'], 0)
    'a'
    >>> concatena_strings(['a',''], 0)
    'a'
    >>> concatena_strings(['',''], 0)
    ''
    >>> concatena_strings(['a','casa','verde'], 0)
    'acasaverde'
    '''
    if x == len(lst):
        string = ''
    else:    
        string = lst[x] + concatena_strings(lst, x+1)
    return string
