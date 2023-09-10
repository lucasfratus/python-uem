from enum import Enum, auto
from dataclasses import dataclass
# Analise
# Determina qual jogador ganhou o jogo de jokenpo através do simbolo feito por ambos jogadores, mostrando o nome do jogador vencedor.

# Tipos de dados
# O nome do jogador será uma estrutura
# O simbolo feito por cada jogador será uma estrutura

class Simbolo(Enum):
    '''
    Simbolo feito por cada jogador
    '''
    PEDRA = auto()
    TESOURA = auto()
    PAPEL = auto()

class Resultado(Enum):
    '''
    Resultado da jogada
    '''
    PRIMEIRO = auto()
    SEGUNDO = auto()
    EMPATE = auto()


def jokenpo(a: Simbolo, b: Simbolo) -> Resultado:
    '''
    Determina qual jogador ganhou um jogo de jokenpo através do simbolo jogado por cada um deles, retornando o nome do vencedor.
    Simbolo.PEDRA vence simbolo.TESOURA. Simbolo.Tesoura vence Simbolo.PAPEL. Simbolo.PAPEL vence Simbolo.PEDRA. 
    Exemplos
    >>> jokenpo(Simbolo.PEDRA,Simbolo.TESOURA).name
    'PRIMEIRO'
    >>> jokenpo(Simbolo.TESOURA,Simbolo.PEDRA).name
    'SEGUNDO'
    >>> jokenpo(Simbolo.PEDRA,Simbolo.PEDRA).name
    'EMPATE'
    '''
    if a == b:
        resultado = Resultado.EMPATE
    elif (a == Simbolo.PEDRA and b == Simbolo.TESOURA) or \
            (a == Simbolo.PAPEL and b == Simbolo.PEDRA) or \
            (a == Simbolo.TESOURA and b == Simbolo.PAPEL):
        resultado = Resultado.PRIMEIRO
    else:
        resultado = Resultado.SEGUNDO
    return resultado
        

