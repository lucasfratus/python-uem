# Analise
# Verifica se um número especifico está em uma lista de inteiros.
# Tipos de dados
# A lista será composta de inteiro
# O número será um inteiro

def verifica_n(n: int, lst: list[int], x: int) -> bool:
    '''
    Devolve True caso *n* estiver em *lst*.Caso contrário, devolve False. *x* é sempre 0.
    Exemplos:
    >>> verifica_n(3,[],0)
    False
    >>> verifica_n(3,[0,3],0)
    True
    >>> verifica_n(7,[5,6],0)
    False
    >>> verifica_n(5,[1,2,5,7,8],0)
    True
    >>> verifica_n(1,[1,2,5,7,8],0)
    True
    >>> verifica_n(8,[1,2,5,7,8],0)
    True
    '''
    if x == len(lst):
        verificacao = False
    else:
        if lst[x] == n:
            verificacao = True
        else:
            verificacao = verifica_n(n, lst, x+1)
    return verificacao