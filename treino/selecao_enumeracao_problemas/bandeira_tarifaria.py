from enum import Enum, auto
# Analise
# Calcula quanto deve ser pago em uma tarifa de energia, com base no consumo em quilowatt-hora, tarifa básica do quilowatt-hora e a bandeira
# tarifaria.
# Cada cor de bandeira indica um acrescimo no valor da energia:
# Bandeira Verde não sofre acrescimo no valor da energia.
# Bandeira Amarela sofre acréscimo de R$ 0,01874 para cada quilowatt-hora consumido.
# VERMELHA 1 sofre acrescimo de R$ 0,03971 para cada quilowatt-hora consumido.
# VERLMELHA 2 sofre acrescimo de R$ 0,09492 para cada quilowatt-hora consumido

# Tipos de dados
# O consumo será representado em quilowatt-hora e será um float positivo.
# O valor do quilowatt-hora será representado em reais e será um float positivo.
# A bandeira tarifária será um tipo enumerado

class Bandeira(Enum):
    '''
    classificação da bandeira tarifária
    '''
    VERDE = auto()
    AMARELA = auto()
    VERMELHA1 = auto()
    VERMELHA2 = auto()

def bandeira_tarifaria(valor: float,consumo: float, bt: Bandeira) -> float:
    '''
    Calcula quanto vai ser pago na tarifa de energia, com dado consumo em quilowatt-hora, o valor de cada quilowatt-hora
    e qual a bandeira tarifária do momento. Cada tipo de *bt* indica um acrescimo na tarifa de energia:
    Bandeira.VERDE não sofre acrescimo no valor da energia.
    Bandeira.AMARELA sofre acréscimo de R$ 0,01874 para cada quilowatt-hora consumido.
    Bandeira.VERMELHA1 sofre acrescimo de R$ 0,03971 para cada quilowatt-hora consumido.
    Bandeira.VERLMELHA2 sofre acrescimo de R$ 0,09492 para cada quilowatt-hora consumido.
    Exemplos
    >>> bandeira_tarifaria(100.00,800.00,Bandeira.VERDE)
    100.00
    >>> bandeira_tarifaria(100.00,800.00,Bandeira.AMARELA)
    114.992
    >>> bandeira_tarifaria(100.00,800.00,Bandeira.VERMELHA1)
    131.768
    >>> bandeira_tarifaria(100.00,800.00,Bandeira.VERMELHA2)
    175.936
    '''
    if bt == Bandeira.VERDE:
        tarifa = valor + consumo * 0
    elif bt == Bandeira.AMARELA:
        tarifa = valor + consumo * 0.01874
    elif bt == Bandeira.VERMELHA1:
        tarifa = valor + consumo * 0.03971
    else: # bt == Bandeira.VERMELHA2
        tarifa = valor + consumo * 0.09492
    return tarifa
