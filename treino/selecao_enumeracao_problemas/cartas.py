from dataclasses import dataclass
from enum import Enum, auto
# Analise
# Classifica uma sequencia de 3 cartas em crescente, decrescente ou não ordenada. As cartas são enumeradas de 1 a 13.

# Tipo de dados
# A sequencia de 3 cartas terá sua propria estrutura

@dataclass
class Carta:
    '''
    Cartas A,B,C , que possuem valores entre 1 a 13.
    '''
    a: int
    b: int
    c: int

class Ordem(Enum):
    '''
    Ordem das cartas
    '''
    CRESCENTE = auto()
    DECRESCENTE = auto()
    NAO_ORDENADO = auto()

def ordem_cartas(c: Carta) -> Ordem:
    '''
    Classica a sequência de 3 cartas *c*(Carta.A, Carta.B, Carta.C), classificando-as em:
    Ordem.CRESCENTE, Ordem.DESCRESCENTE e Ordem.NAO_ORDENADO.
    Exemplos
    >>> ordem_cartas(Carta(3,4,5)).name
    'CRESCENTE'
    >>> ordem_cartas(Carta(5,3,2)).name
    'DECRESCENTE'
    >>> ordem_cartas(Carta(2,1,4)).name
    'NAO_ORDENADO'
    '''
    if c.a < c.b and c.b < c.c:
        classificacao = Ordem.CRESCENTE
    elif c.c > c.b and c.b > c.c:
        classificacao = Ordem.CRESCENTE
    else:
        classificacao = Ordem.NAO_ORDENADO
    return classificacao
