# Análise
# Calcular o tempo gasto para pintar um paralelepípedo.
# A cada 30 segundos, é pintada uma área de 8 cm x 8 cm
# Se a cada 30 segundos, ele pinta uma área de 64cm², em um segundo ele pinta aproximadamente 2.13 cm

# Tipos de dados
# A altura e comprimento serão dados em centímetros e representados por números positivos.
# O tempo será dado em segundos e representado por números inteiros.

def tempo_paralelepipedo(comprimento: float, largura: float)-> float:
  '''
  Calcula o tempo necessário para pintar um paralelepípedo a partir de suas dimensões.

  Exemplos
  >>> # (10 * 8) / 2.13
  >>> round(tempo_paralelepipedo(10,8),2)
  37.56
  '''
  area = comprimento * largura
  return area / 2.13