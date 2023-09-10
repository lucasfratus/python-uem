# Analise
# Verifica se a quantidade de elementos de uma lista de floats é menor que 4

# Tipos de dados
# A lista é composta de floats.

def menor_que_4(lst: list[float]) -> bool:
    '''
    Verifica se *lst* possui menos que 4 elementos.
    Exemplos
    >>> menor_que_4([1.3,2.4,3.1])
    True
    >>> menor_que_4([1.7,2.0,3.1,4.5])
    False
    >>> menor_que_4([1.2,2.55,3.7,4.1,5.0])
    False
    '''
    if len(lst) < 4:
        verificacao = True
    else:
        verificacao = False
    return verificacao