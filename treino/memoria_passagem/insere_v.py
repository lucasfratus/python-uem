# Analise
# Insere um valor v em um indice i de uma lista de inteiros.
#
# Tipos de dados
# O valor v será um número inteiro.
# Indice i será um número inteiro não negativo.
# A lista será composta de inteiros.

def insere_v(v: int, indice: int, lst: list[int]):
    '''
    Insere *v* no indice *i* de *lst*.*lst* não pode ser uma lista vazia.
    Exemplos:
    >>> lst = [1,2,3,4]
    >>> insere_v(3,0,lst)
    >>> lst
    [3, 1, 2, 3, 4]
    >>> lst = [1,2,3,4]
    >>> insere_v(2,4,lst)
    >>> lst
    [1, 2, 3, 4, 2]
    '''
    lst.append(v)

    for x in range(len(lst)):
        if x == indice:
            elemento = lst[x]
            lst[x] = lst[len(lst)-1]
            lst[len(lst)-1] = elemento
        if x > indice:
            elemento = lst[len(lst)-1]
            lst[len(lst)-1] = lst[x]
            lst[x] = elemento

        



