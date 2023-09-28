# Análise
# Calcular o tempo gasto para pintar um paralelepípedo.
# A cada 30 segundos, é pintada uma área de 8 cm x 8 cm
# Se a cada 30 segundos, ele pinta uma área de 64cm², em um segundo ele pinta aproximadamente 2.13 cm

# Tipos de dados
# A altura e comprimento serão dados em centímetros e representados por números positivos.
# O tempo será dado em segundos e representado por números inteiros.

tempo_por_metro_quadrado: float = 2.13

def tempo_paralelepipedo(comprimento: float, largura: float) -> float:
    '''
    Calcula o tempo necessário para pintar um paralelepípedo a partir de sua área, calculada pelo produto 
    entre *comprimento* e *altura*.
  
    Exemplos
    >>> # (10 * 10) / 2.13
    >>> round(tempo_paralelepipedo(10,10),2)
    46.95
    >>> # (15 * 15) / 2.13
    >>> round(tempo_paralelepipedo(15,15),2)
    105.63
    '''
    area = comprimento * largura
    return area / tempo_por_metro_quadrado