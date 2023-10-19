# Analise
# Cria uma nova lista de inteiros a partir de uma lista de strings, convertendo cada string para um inteiro.
# Tipos de dados
# A lista será composta de strings

def transformar_str_int(lst: list[str],lst_nova: list[int], x: int) -> list[int]:
    '''
    Cria uma nova lista de inteiros a partir de *lst*, convertendo cada string de *lst* em um inteiro. *x* precisa ser 0
    *lst_nova* deve ser uma lista vazia.
    Exemplos:
    >>> transformar_str_int(['1','2','3'],[],0)
    [1, 2, 3]
    >>> transformar_str_int([],[],0)
    []
    >>> transformar_str_int(['-1','0','3'],[],0)
    [-1, 0, 3]
    '''
    if x == len(lst):
        resultado = lst_nova
    else:
        lst_nova.append(int(lst[x]))
        resultado = transformar_str_int(lst,lst_nova,x+1)
    return resultado
