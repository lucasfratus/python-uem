from enum import Enum, auto
# Analise
# Verifica se o nome dado é curto, longo ou mediano. Um nome é curto se possui no maximo quatro letras e longo se possui mais que 8.
# Um nome que não é curto nem longo é mediano.

# Tipos de dados
# O nome será uma string.

class Tamanho(Enum):
    '''
    classificação do tamanho do nome
    '''
    CURTO = auto()
    MEDIANO = auto()
    LONGO = auto()

def tamanho_nome(nome: str) -> Tamanho:
    '''
    Classica se *nome* é curto,mediano ou longo. Um nome curto possui no máximo quatro letras.
    Um nome longo possui mais de 8 letras.
    Um nome mediano não é curto nem longo, ou seja, possui mais de 4 letras e menos de 8 letras(ou 8 letras).
    Na contagem de letras, espaços são incluidos.
    Exemplos
    >>> tamanho_nome('Ana').name
    'CURTO'
    >>> tamanho_nome('Lucas').name
    'MEDIANO'
    >>> tamanho_nome('Joao Pedro').name
    'LONGO'
    '''
    if len(nome) <= 4:
        classificacao = Tamanho.CURTO
    elif len(nome) > 4 and len(nome) <= 8:
        classificacao = Tamanho.MEDIANO
    else: #len(nome) > 8
        classificacao = Tamanho.LONGO
    return classificacao

