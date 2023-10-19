def soma(lst: list[int], i: int) -> list[int]:
    '''
    Soma todos os elementos de *lst* até o indice *i*(lst[:i])
    de maneira recursiva *i* necessita ser menor que len(lst) e maior que zero
    Exemplos:
    >>> soma([1,2,3],3)
    6
    >>> soma([0],0)
    0
    >>> soma([],0)
    0
    '''
    if i <= 0:
        s = 0
    else:
        s = lst[i-1] + soma(lst, i-1)
    return s