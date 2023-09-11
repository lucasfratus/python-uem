# Análise
# Cria uma nova lista,somando um valor a cada elemento de uma lista de números.

# Tipos de dados
# Todos os elementos da lista serão números inteiros.
# O valor somado a cada elemento da lista é um número inteiro

def valor_x(lst: list[int], x: int) -> list:
    '''
    Criar uma nova lista após somar um valor *x* de uma lista *lst* de inteiros.
    >>> valor_x([1,2,3],1)
    [2,3,4]
    >>> valor_x([2,-1,3],2)
    [4,1,5]
    '''
    resposta = []
    for n in lst:
        n = n + x
        resposta.append(n)
    return resposta