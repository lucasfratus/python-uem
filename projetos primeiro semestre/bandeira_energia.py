# Análise
# Determinar o valor final da tarifa de energia, considerando o consumo quilowatt-hora, o valor do kW/h
# e a bandeira tarifaria.
#
# Tipos de Dados
# O consumo em quilowatt-hora será dado em um número flutuante positivo.
# O valor do quiilowatt-hora será um número flutuante positivo.
# A bandeira tarifária terá seu tipo próprio.

from enum import Enum, auto
class bandeira(Enum):
    '''cor da bandeira tarifaria'''
    VERDE:auto()
    AMARELA:auto()
    VERMELHA1:auto()
    VERMELHA2:auto()


def valor_energia(tarifa_original,kwh : float,bandeira_tarifaria: bandeira) -> str:
    '''
    Calcula o valor final da tarifa de energia, somando o valor da *tarifa_original* com o produto 
    entre o consumo em kW/h e o valor da *bandeira_tarifaria*
    
    Exemplos:
    >>> valor_energia(10,10,VERDE)
    10
    >>> valor_energia(20.10,AMARELA)
