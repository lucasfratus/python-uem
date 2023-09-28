# Análise
# Determinar o valor final da tarifa de energia, considerando o consumo quilowatt-hora, o valor do kW/h \
# e a bandeira tarifaria.
#
# Tipos de Dados
# O consumo em quilowatt-hora será dado em um número flutuante positivo.
# O valor do quiilowatt-hora será um número flutuante positivo.
# A bandeira tarifária terá seu tipo próprio tipo.

from enum import Enum, auto
class bandeira(Enum):
    '''cor da bandeira tarifaria'''
    VERDE=auto()
    AMARELA=auto()
    VERMELHA1=auto()
    VERMELHA2=auto()

def valor_energia(tarifa_original, kwh: float, bandeira_tarifaria: bandeira) -> float:
    '''
    Calcula o valor final da tarifa de energia, somando o valor da *tarifa_original* com o produto  
    entre o consumo em kWh e o valor da *bandeira_tarifaria*. A bandeira tarifária possui 4 tipos: VERDE 
    (tarifa não sofre acrescimo), AMARELA(acréscimo de R$ 0,01874 por quilowatt-hora), VERMELHA - patamar 1(acréscimo 
    de R$ 0,03971 por quilowatt-hora) e VERMELHA - patamar 2(acréscimo de R$ 0,09492 por quilowatt-hora).
    Exemplos:
    >>> roundvalor_energia(100.00,10.00,bandeira.VERDE)
    100.00
    >>> round(valor_energia(200.00,100.00,bandeira.AMARELA),2)
    201.87
    >>> round(valor_energia(150.00,110.00,bandeira.VERMELHA1),2)
    154.37
    >>> round(valor_energia(170.00,130.00,bandeira.VERMELHA2),2)
    182.34
    '''
    if bandeira_tarifaria == bandeira.VERDE:
        valor_bandeira = 0
    elif bandeira_tarifaria == bandeira.AMARELA:
        valor_bandeira = 0.01874
    elif bandeira_tarifaria == bandeira.VERMELHA1:
        valor_bandeira = 0.03971
    else:
        valor_bandeira = 0.09492
    
    return tarifa_original + (kwh * valor_bandeira)
    
