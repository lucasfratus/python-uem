from enum import Enum, auto
from dataclasses import dataclass
# Analise
# Indica qual o número máximo de casas de um tabuleiro que um personagem pode avançar na direção em que ele está virado. As linhas e as colunas
# desse tabuleiro são enumeradas de 1 a 10, podendo a posição do personagem ser determinada por linha x coluna. O personagem fica virado para as direções norte
# sul, leste ou oeste. O personagem pode avançar para qualquer casa na direção que ele está virado, não saindo do tabuleiro.

# Tipos de dados
# A direção do personagem será um tipo enumerado.
# As linhas e colunas do tabuleiro são inteiros positivos de 1 a 10.
# A direção e a posição do personagem serão representados em uma estrutura.

class Direcao(Enum):
    '''
    Representa a direção que o personagem está virado no tabuleiro
    '''
    NORTE = auto()
    SUL = auto()
    LESTE = auto()
    OESTE = auto()

@dataclass
class Personagem:
    '''
    Representa as informações do personagem no tabuleiro
    '''
    linha: int
    coluna: int
    direcao_virado: Direcao

def casas_tabuleiro(p: Personagem) -> int:
    '''
    Indica o número maximo de casas de um tabuleiro que *p* pode avançar na direção em que está virado.
    - As linhas e colunas são enumeradas de 1 a 10.
    *p* pode avançar para qualquer casa na direção em que ele está virado, não podendo sair do tabuleiro.
    - Quando *p* estiver virado para Direcao.NORTE ou Direcao.SUL, apenas o número de linhas é 
    considerado na contagem de casas que pode avançar.
    - Quando *p* estiver virado para Direcao.LESTE ou Direcao.OESTE, apenas o número de colunas 
    é considerado na contagem de casas que pode avançar
    Exemplos
    >>> casas_tabuleiro(Personagem(1,5,Direcao.NORTE))
    9
    >>> casas_tabuleiro(Personagem(1,3,Direcao.LESTE))
    2
    >>> casas_tabuleiro(Personagem(2,4,Direcao.OESTE))
    6
    >>> casas_tabuleiro(Personagem(4,3,Direcao.SUL))
    3
    '''
    if p.direcao_virado == Direcao.NORTE:
        casas_maximas = 10 - p.linha
    elif p.direcao_virado == Direcao.SUL:
        casas_maximas = p.linha - 1
    elif p.direcao_virado == Direcao.OESTE:
        casas_maximas = 10 - p.coluna
    else: # p.direcao_virado == Direcao.LESTE:
        casas_maximas = p.coluna - 1
    return casas_maximas