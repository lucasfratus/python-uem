# Analise
# Calcula a amplitude dos valores de uma lista não vazia de números.
# Tipos de dados
# A lista será composta de inteiros

def amplitude(lst: list[int]) -> int:
    '''
    Calcula a amplitude dos valores de *lst*. Ou seja, a diferença entre o maior e o menor. *lst* não pode ser vazia
    Exemplos:
    >>> amplitude([1,2])
    1
    >>> amplitude([3,7])
    4
    >>> amplitude([12,3,6,10,])
    9
    '''
    assert len(lst) > 0
    i = 0
    maximo = lst[0]
    # Definindo o maximo
    while i < len(lst):
        if lst[i] > maximo:
            maximo = lst[i]
        i = i + 1
    
    o = 0
    minimo = lst[0]
    # Definindo o mínimo
    while o < len(lst):
        if lst[o] < minimo:
            minimo = lst[o]
    
    # Calculo da amplitude
    calculo_amplitude = maximo - minimo
    return calculo_amplitude
