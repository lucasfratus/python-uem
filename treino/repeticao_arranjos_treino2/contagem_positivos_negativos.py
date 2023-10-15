from enum import Enum, auto
# Analise
# Indica se uma lista possui mais valores positivos ou negativos.
# Tipos de dados
# A lista será composta por inteiros.

class Sinal(Enum):
    ''' 
    Representa a quantidade de números positivos e negativos de uma lista. Caso for zero, é representado como nulo.
    '''
    POSITIVO = auto()
    NEGATIVO = auto()
    IGUAL = auto()
    NULO = auto()

def contagem(lst: list[int]) -> Sinal:
    '''
    Indica se *lst* possui mais números positivos ou negativos.
    Exemplos:
    >>> contagem([0])
    <Sinal.NULO: 4>
    >>> contagem([-1,1])
    <Sinal.IGUAL: 3>
    >>> contagem([-1,1,2])
    <Sinal.POSITIVO: 1>
    >>> contagem([-1,-2,0,1])
    <Sinal.NEGATIVO: 2>
    '''
    i = 0
    contagem_positivo = 0
    contagem_negativo = 0
    contagem_zero = 0
    while i < len(lst):
        if lst[i] < 0:
            contagem_negativo = contagem_negativo + 1
        if lst[i] == 0:
            contagem_zero = contagem_zero + 1
        if lst[i] > 0:
            contagem_positivo = contagem_positivo + 1
        i = i + 1
    if contagem_positivo > contagem_negativo and contagem_positivo > contagem_zero:
        resultado = Sinal.POSITIVO
    elif contagem_negativo > contagem_positivo and contagem_negativo > contagem_zero:
        resultado = Sinal.NEGATIVO
    elif contagem_zero > contagem_positivo and contagem_zero > contagem_negativo:
        resultado = Sinal.NULO
    elif contagem_zero == contagem_positivo and contagem_zero == contagem_negativo or contagem_positivo == contagem_negativo and \
        contagem_zero == 0:
        resultado = Sinal.IGUAL
    return resultado