from enum import Enum, auto
# Analise
# Indica se a lista de inteiros possui mais valores positivos do que negativos

# Tipos de dados
# A lista é composta de números inteiros.

class Sinal(Enum):
    '''
    Representa o sinal de cada elemento inteiro de uma lista
    
    '''
    POSITIVOS: auto()
    NEGATIVOS: auto()
    QUANTIDADE_IGUAL: auto()

def positivos_negativos(lst: list[int]) -> Sinal:
    '''
    Indica se lst possui mais valores positivos do que negativos. A lista *lst* não pode ser vazia. O número 'zero' não assume sinal,
    então não entra para a contagem de positivos ou negativos.
    Exemplos:
    >>> positivos_negativos([1,-1,1]).name
    'POSITIVOS'
    >>> positivos_negativos([0,1,-2,-3]).name
    'NEGATIVOS'
    >>> positivos_negativos([0,1,2.-2,-2]).name
    'QUANTIDADE_IGUAL'
    '''
    contagem_positivos = 0
    contagem_negativos = 0
    # Contagem dos números positivos.
    for x in lst:
        if x > 0:
            contagem_positivos = contagem_positivos + 1
    
    # Contagem dos números negativos
    for x in lst:
        if x < 0:
            contagem_negativos = contagem_negativos + 1
    
    # Comparação entre positivos e negativos.
    if contagem_positivos > contagem_negativos:
        contagem_total = Sinal.POSITIVOS
    elif contagem_positivos < contagem_negativos:
        contagem_total = Sinal.NEGATIVOS
    else: # contagem_positivos ==  contagem_negativos
        contagem_total = Sinal.QUANTIDADE_IGUAL
    return contagem_total
      
