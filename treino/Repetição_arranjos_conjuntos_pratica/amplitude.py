# Analise
# Calcula a amplitude entre o maior e o menor valor de uma lista não vazia.

# Tipos de dados
# a lista será composta de números inteiros.

def amplitude1(lst: list[int]) -> int:
    '''
    Calcula a amplitude entre o maior valor e o menor de *lst*. *lst* não pode ser uma lista vazia
    Exemplos
    >>> amplitude1([1,4,5])
    4
    >>> amplitude1([1])
    0
    >>> amplitude1([-1,3,4])
    5
    '''
    assert len(lst) != 0
    maior_valor = lst[0]
    # Definir maior valor de *lst*
    for x in lst:
        if x > maior_valor:
            maior_valor = x
    
    menor_valor = lst[0]
    # Definir o menor valor de *lst*
    for x in lst:
        if x < menor_valor:
            menor_valor = x
    
    # Definir amplitude
    amplitude = maior_valor - menor_valor
    return amplitude

def amplitude2(lst: list[int]) -> int:
    assert len(lst) !=0
    maior_valor = lst[0]
    menor_valor = lst[0]
    for x in lst:
        if x > maior_valor:
            maior_valor = x
                
        return maior_valor - menor_valor