# Análise
# Converte uma medida em centimetro para polegadas.

# Tipos de dados
# A medida será dada em centimetros e é um número flutuante positivo

def centimetro_polegada(medida: float) -> float:
    '''
    Converter uma medida em centimetro para polegada. Uma polegada equivale a 2.54 centímetros. A medida precisa ser positiva.
    Exemplos:
    >>> (2.54)
    1.0 
    >>> (5.08)
    2.0
    >>> (0.0)
    0.0
    '''
    POLEGADA_EM_CENTIMETROS = 2.54
    return medida / POLEGADA_EM_CENTIMETROS
