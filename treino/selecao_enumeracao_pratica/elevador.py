from enum import Enum, auto
# Analise
# Representa o estado de um elevador, podendo estar parado, descendo ou subindo.

# Tipos de dados
# O estado do elevador será representado por uma enumeração.

class Estado(Enum):
    '''
    Estado do eleveador
    '''
    PARADO = auto()
    DESCENDO = auto()
    SUBINDO = auto()

def a_elevador(andar_atual, andar_solicitado: int) -> Estado:
    '''
    Determina, a partir de *andar_atual* e *andar_solicitado*, qual será a condição do elevador ao atender a solicitação.
    Exemplos
    >>> a_elevador(2,5).name
    'SUBINDO'
    >>> a_elevador(7,2).name
    'DESCENDO'
    >>> a_elevador(3,3).name
    'PARADO'
    '''
    if andar_solicitado > andar_atual:
        condicao = Estado.SUBINDO
    elif andar_solicitado < andar_atual:
        condicao = Estado.DESCENDO
    else: # andar_solicitado = andar_atual
        condicao = Estado.PARADO
    return condicao

def b_elevador(estado: Estado) -> bool:
    '''
    Verifica se um elevador pode passar de um *estado* para outro. Um elevador apenas começa a se movimentar se estiver parado.
    
                    possibilidades
    estado
    PARADO     ->   PARAR *SUBIR* *DESCER*
    SUBINDO    ->   *PARAR* SUBIR DESCER
    DESCENDO   ->   *PARAR* SUBIR DESCER
    As possibilidades entre * são as que produzem True. O resto produz False
    '''
    if estado == Estado.PARADO:
        if a_elevador() == Estado.PARADO:
            verificacao = False
        elif a_elevador() == Estado.SUBINDO:
            verificacao = True
        elif a_elevador() == Estado.PARADO:
            verificacao = True
    elif estado == Estado.SUBINDO:
        if a_elevador() == Estado.PARADO:
            verificacao = True
        else: # a_elevador() == Estado.SUBINDO or a_elevador() == Estado.DESCENDO 
            verificacao = False
    else: # estado == Estado.DESCENDO:
        if a_elevador() == Estado.PARADO:
            verificacao = True
        else: # a_elevador() == Estado.SUBINDO or a_elevador() == Estado.DESCENDO 
            verificacao = False
    return verificacao




