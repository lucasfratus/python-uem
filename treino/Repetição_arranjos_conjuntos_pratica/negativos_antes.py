# Analise
# Cria uma nova lista a partir de outra lista, colocando os números negativos antes dos positivos

# Tipos de dados
# A lista será composta de números inteiros.

def negativos_antes(lst: list[int]) -> list[int]:
    '''
    Cria uma nova lista a partir de *lst*, colocando os números negativos antes dos positivos. O número zero fica entre os negativos
    e positivos.
    Exemplos
    >>> negativos_antes([1,0,-1])
    [-1,0,1]
    >>> negativos_antes([-1,1,3,-2])
    [-1,-2,1,3]
    '''
    positivos = []
    negativos = []
    nulos = []
    for x in lst:
        if x > 0:
            positivos.append(x)
        elif x < 0:
            negativos.append(x)
        else: # x == 0
            nulos.append(x)
    # Juntando positivos, negativos e nulos
    return negativos + nulos + positivos