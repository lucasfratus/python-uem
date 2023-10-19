# Analise
# Remove as strings vazias de uma lista de strings.
# Tipos de dados
# A lista será composta de strings.

def remove_str_vazias(lst: list[str]):
    '''
    Remove todas as strings vazias de *lst*
    Exemplos:
    >>> lst = ['']
    >>> remove_str_vazias(lst)
    >>> lst
    []
    >>> lst = ['a','']
    >>> remove_str_vazias(lst)
    >>> lst
    ['a']
    >>> lst =['b','c']
    >>> remove_str_vazias(lst)
    >>> lst
    ['b', 'c']
    '''
    i = 0
    while i < len(lst):
        if lst[i] == '':
            t = lst[i]
            lst[i] = lst[len(lst)-1]
            lst[len(lst)-1] = t
            lst.pop()
        i = i + 1

    
