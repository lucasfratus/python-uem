# Analise
# Devolve uma lista de números recebida, porém sem o elemento de uma posição especificada dessa lista.

# Tipos de dados
# A posição a ser removida é um inteiro positivo
# A lista é composta de inteiros.
def remove1(posicao: int, lst: list[int]) -> list[int]:
    '''
    Devolve uma lista a partir de *lst*, porém sem o elemento de *posição*. *lst* não pode ser vazia e a posição precisa ser menor que
    o número de elementos de *lst*.
    Para resolver, é possivel somar os elementos de *lst* antes da posição dada e os elementos depois da posição.
    Exemplos:
    >>> remove1(1,[2,3,5])
    [2,5]
    >>> remove1(2,[3,4,5,6])
    [3,4,6]
    >>> remove1(0,[3,4,5,7])
    [4,5,7]
    '''  
    assert len(lst) != 0
    assert 0 < posicao < len(lst)
    lista_sem = []
    # Antes de posição
    for x in range(posicao):
        lista_sem.append(lst[x])

    # Depois da posição
    for x in range(posicao + 1,len(lst)):
        lista_sem.append(lst[x])
    
    return lista_sem

def remove2(posicao: int, lst: list[int]) -> list[int]:
    '''
    Devolve uma lista a partir de *lst*, porém sem o elemento de *posição*. *lst* não pode ser vazia
    Exemplos:
    >>> remove2(1,[2,3,5])
    [2,5]
    >>> remove2(2,[3,4,5,6])
    [3,4,6]
    >>> remove2(7,[3,4,5,7])
    [3,4,5,7]
    '''
    assert len(lst) != 0
    lista_sem = []
    for x in range(len(lst)):
        if x != posicao:
            lista_sem.append(lst[x])
    return lista_sem

def remove3(posicao: int, lst: list[int]) -> list[int]:
    lista_ate_posicao = lst[:posicao]
    lista_apos_posicao = lst[(posicao + 1):]
    return lista_ate_posicao + lista_apos_posicao

# A função remove3 é a mais simples e não usa repetição, apenas operações de sublistas.
# A função remove2 usa apenas uma repetição, o que acaba deixando o código mais dificil de compreender
# Já a função remove1 utiliza duas repetições, dividindo o código em duas etapas, deixando o código mais facil de compreender.

        

