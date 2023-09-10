# Analise
# Calcula quanto tempo demora para pintar a área total de um paralelepípedo. 

# Tipos de dados.
# As dimensões do paralelepipedo(largura,altura e comprimento) serão dadas em centimetros e serão floats positivos.
# O tempo que leva para cada centimetro ser pintado será dado em segundos e é um float positivo,

TEMPO_POR_CM_QUADRADO: float = 2.13
def tempo_paralelepipedo(comprimento, altura, largura: float) -> float:
    '''
    Calcular quanto tempo demora para pintar a área total de um paralelepípedo. 
    A medida de cada base é calculada através produto entre *largura* e *comprimento*.
    A medida de cada face lateral é calculada através do produto entre *altura* e *comprimento*.
    A área total é calculada pela soma das duas bases com as quatro faces do paralelepípedo.
    Todas as medidas do paralelepípedo devem ser maiores que 0
    Cada centímetro quadrado demora 2.13 segundos para ser pintado.
    Exemplos:
    >>> round(tempo_paralelepipedo(1,2,1),2)
    21.3
    >>> (3,3,3)
    115.02
    '''
    area_base = largura * comprimento
    area_face_lateral = altura * comprimento
    area_total = 2 * area_base + 4 * area_face_lateral
    return area_total * TEMPO_POR_CM_QUADRADO
