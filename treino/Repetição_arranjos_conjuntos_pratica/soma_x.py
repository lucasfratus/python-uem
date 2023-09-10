# Analise
# Cria uma nova lista somando um valor x em cada elemento da lista de inteiros.

# Tipos de dados
# Os elementos da lista serão números inteiros.
# O valor x será um número inteiro.

def soma_x(lst: list[int], n: int) -> list[int]:
    '''
    Soma um valor *n* a todos os elementos de *lst*, criando uma nova lista. *lst* não pode ser uma lista vazia.
    >>> soma_x([1,3,4],1)
    [2,4,5]
    >>> soma_x([1],10)
    [11]
    '''
    lista = []
    for x in lst:
        lista.append(x + 1)
    return lista