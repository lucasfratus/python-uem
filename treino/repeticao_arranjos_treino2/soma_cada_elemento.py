# Analise
# Soma um valor específico a cada elemento de uma lista de inteiros.
#
# Tipos de dados
# O valor será um número inteiro.
# A lista será composta de números inteiros.

def soma_cada_elemento(valor: int, lst: list[int]) -> list[int]:
    '''
    Cria uma nova lista a partir de *lst*, somando *valor* a cada elemento de *lst*.
    Exemplos:
    >>> soma_cada_elemento(1,[1,2,3])
    [2, 3, 4]
    >>> soma_cada_elemento(0,[1,2,3])
    [1, 2, 3]
    >>> soma_cada_elemento(3,[7,8,11,2])
    [10, 11, 14, 5]
    '''
    nova_lista = []
    for x in lst:
        soma = x + valor
        nova_lista.append(soma)
    return nova_lista
