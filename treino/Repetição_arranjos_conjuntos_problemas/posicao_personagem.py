from enum import Enum, auto
from dataclasses import dataclass

# Analise
# Calcula a nova posição de um personagem de um jogo a partir de uma sequencia de deslocamentos recebida.
# Cada posição do mapa do jogo é possui uma coordenada(X,Y e Z);
# Cada componenete dessa coordenada pode receber qualquer valor inteiro.
# O personagem pode se deslocar uma unidade por vez. para o norte, sul, leste, oeste e para cima ou para baixo.

# Tipos de dados
# O deslocamento será um entre 6 valores, então será representado por uma enumeração
# A posição é composta por 3 componentes(X,Y e Z), então será representada por uma estrutura

@dataclass
class Coordenadas:
    '''
    Representa a posição em coordenadas do personagem
    '''
    x: int
    y: int
    z: int

class Direcao(Enum):
    '''
    Representa a direção que o personagem irá se deslocar
    NORTE(+) e SUL(-) correspondem ao eixo x
    LESTE(+) e OESTE(-) correspondem ao eixo y
    CIMA(+) e BAIXO(-) correspondem ao eixo Z
    '''
    NORTE = auto()
    SUL = auto()
    LESTE = auto()
    OESTE = auto()
    CIMA = auto()
    BAIXO = auto()



def posicao(p: Coordenadas, lst: list[Direcao]) -> Coordenadas:
    '''
    Define uma nova posição, dividida em (x,y,z), a partir da posição *p* de um personagem e uma lista *lst* de direções.
    O personagem move apenas uma unidade a cada direção dada.
    Exemplos
    >>> posicao(Coordenadas(10,2,10),[Direcao.NORTE,Direcao.LESTE])
    Coordenadas(x=11,y=3,z=10)
    >>> posicao(Coordenadas(10,2,10),[])
    Coordenadas(x=10,y=2,z=10)
    >>> posicao(Coordenadas(10,2,10),[Direcao.CIMA])
    Coordenadas(x=10,y=2,z=11)
    '''
    x = p.x
    y = p.y
    z = p.z
    for d in lst:
        if d == Direcao.NORTE:
            x = x + 1
        elif d == Direcao.SUL:
            x = x - 1
        elif d == Direcao.LESTE:
            y = y + 1
        elif d == Direcao.OESTE:
            y = y - 1
        elif d == Direcao.CIMA:
            z = z + 1
        elif d == Direcao.BAIXO:
            z = z - 1
    return Coordenadas(x,y,z)