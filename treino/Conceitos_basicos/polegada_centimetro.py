# Análise
# Converter uma medida dada em polegadas para centimetros

# Tipos de dados
# A medida em polegadas é um número flutuante positivo

def polegada_centimetro(medida: float) -> float:
    '''
    Converte uma medida em polegadas para centímetros. Cada polegada corresponde a 2.54 centímetros. A medida necessita ser positiva.
    Exemplos:
    >>> (10.0)
    25.4
    >>> (1.0)
    2.54
    >>> (0.0)
    0.0
    '''
    POLEGADA_EM_CENTIMETRO = 2.54
    return medida * POLEGADA_EM_CENTIMETRO
