# Analise
# Verifica se todos os elementos de uma lista de inteiros são binarios, ou seja, são 0 ou 1.
# Tipos de dados
# A lista será composta de inteiros.
def lista_binaria(lst: list[int], x:int) -> bool:
    '''
    Produz True se todos os elementos de *lst* são 0 ou 1. Caso contrário, produz False. *x* deve ser 0.
    >>> lista_binaria([0,1,0,1],0)
    True
    >>> lista_binaria([0,2,0,1],0)
    False
    >>> lista_binaria([0],0)
    True
    '''
    if x == len(lst):
        verificacao = True
    else:
        if lst[x] != 0 and lst[x] != 1:
            verificacao = False
        else:
            verificacao = lista_binaria(lst,x+1)
    return verificacao
    