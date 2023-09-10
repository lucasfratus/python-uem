from enum import Enum, auto

class Direcao(Enum):
    ''' 
    Representa os pontos cardeais, como no esquema a seguir:
          Norte
            |
    Leste -   - Oeste
            |
           Sul
    
    '''
    NORTE = auto()
    SUL = auto()
    LESTE = auto()
    OESTE = auto()

def direcao_oposta(d: Direcao) -> Direcao:
    ''' 
    Indica a direção oposta da direção *d* dada.
    Exemplos
    >>> direcao_oposta(Direcao.NORTE).name
    'SUL'
    >>> direcao_oposta(Direcao.SUL).name
    'NORTE'
    >>> direcao_oposta(Direcao.LESTE).name
    'OESTE'
    >>> direcao_oposta(Direcao.OESTE).name
    'LESTE'
    '''
    if d == Direcao.NORTE:
        oposto = Direcao.SUL
    elif d == Direcao.SUL:
        oposto = Direcao.NORTE
    elif d == Direcao.LESTE:
        oposto = Direcao.OESTE
    else: # if d == Direcao.OESTE
        oposto = Direcao.LESTE
    return oposto

def direcao_90_horario(d: Direcao) -> Direcao:
    '''
    Indica a direção que está a 90 graus no sentido horario de *d*.
    Exemplos
    >>> direcao_90_horario(Direcao.NORTE).name
    'OESTE'
    >>> direcao_90_horario(Direcao.OESTE).name
    'SUL'
    >>> direcao_90_horario(Direcao.SUL).name
    'LESTE'
    >>> direcao_90_horario(Direcao.LESTE).name
    'NORTE'
    '''
    if d == Direcao.NORTE:
        d90 = Direcao.OESTE
    elif d == Direcao.OESTE:
        d90 = Direcao.SUL
    elif d == Direcao.SUL:
        d90 = Direcao.LESTE
    else: # d = Direcao.LESTE
        d90 = Direcao.NORTE
    return d90

def  direcao_90_anti(d: Direcao) -> Direcao:
    '''
    Indica a direção que esta a 90 graus no sentido anti-horario de *d*. Utilizar a função direcao_90_horario na implementaçao desta
    função.
    Exemplos
    >>> direcao_90_anti(Direcao.NORTE).name
    'LESTE'
    >>> direcao_90_anti(Direcao.OESTE).name
    'NORTE'
    >>> direcao_90_anti(Direcao.SUL).name
    'OESTE'
    >>> direcao_90_anti(Direcao.LESTE).name
    'SUL'
    '''
    return direcao_90_horario(direcao_90_horario(direcao_90_horario(d)))   