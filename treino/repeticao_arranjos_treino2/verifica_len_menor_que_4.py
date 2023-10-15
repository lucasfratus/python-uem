# Analise
# Verifica se o tamanho de uma lista de floats é menor que 4.
# Tipos de dados
# A lista será composta por floats.

def verifica_menor_que_4(lst: list[float]) -> bool:
    '''
    Verifica se o tamanho de *lst* é menor que 4. Caso for, produz True. Caso contrário, produz False.
    Exemplos:
    >>> verifica_menor_que_4([])
    True
    >>> verifica_menor_que_4([1.2,2.5,3.0])
    True
    >>> verifica_menor_que_4([1.2,2.3,3.5,6.7])
    False
    >>> verifica_menor_que_4([1.2,2.3,3.5,6.7,7.5])
    False
    '''
    i = 0
    menor_que_4 = True
    while menor_que_4 and i < len(lst):
        if i == 3:
            menor_que_4 = False
        i = i + 1
    return menor_que_4
    