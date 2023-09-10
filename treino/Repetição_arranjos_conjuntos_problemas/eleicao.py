from dataclasses import dataclass
from enum import Enum, auto

# Analise
# Recebe uma lista não vazia de votos e determina qual o ganhador entre dois candidatos. O cnadidato que possuir mais votos é o ganhador.
# Se os votos em branco forem maiores que 50% do total de votos, novas eleições devem ser convocadas.

# Tipos de dados
# A lista será representada pelos candidatos.

@dataclass
class Urna:
    '''
    Representa os parametros de uma urna
    '''
    candidato1: int
    candidato2: int
    branco: int

class Resultado(Enum):
    '''
    Representa o vencedor da eleição
    '''
    PRIMEIRO = auto()
    SEGUNDO = auto()
    EMPATE = auto()
    NOVA_ELEICAO = auto()

def contador_de_votos(lst: list[Urna]) -> list[Urna]:
    '''
    Indica a quantidade de votos para cada candidato da eleição.
    Exemplos
    >>> contador_de_votos([Urna(10,2,3),Urna(2,3,5)])
    (12,5,8)
    '''
    votos_1 = 0
    votos_2 = 0
    votos_brancos = 0
    for x in lst:
        if x.candidato1 > 0:
            votos_1 = votos_1 + x.candidato1
        if x.candidato2 > 0:
            votos_2 = votos_2 + x.candidato2
        if x.branco > 0:
            votos_brancos = votos_brancos + x.branco
    lista_total: list[Urna] = [Urna(votos_1,votos_2,votos_brancos)]
    return lista_total            

def ganhador(lista_total: list[Urna]) -> Resultado:
    '''
    Determina qual o ganhador entre dois candidatos através de uma *lst* de votos. Se os votos em branco forem maiores que 50% do total de votos,
    uma nova eleição deve ser convocada.
    ''' 
    nova_lista = contador_de_votos(lista_total)
    for x in nova_lista:
        if x.branco < (0.5 *(x.candidato1 + x.candidato2)):
            if x.candidato1 > x.candidato2:
                result = Resultado.PRIMEIRO
            elif x.candidato1 < x.candidato2:
                result = Resultado.SEGUNDO
            else:
                result = Resultado.EMPATE
        else:
            result = Resultado.NOVA_ELEICAO
    return result
    
