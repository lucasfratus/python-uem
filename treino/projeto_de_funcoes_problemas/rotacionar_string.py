# Análise
# Rotaciona um texto a direita uma certa quantidade de caracteres. Ou seja, move essa certa quantidade de últimos caracteres para 
# o ínicio do texto.

# Tipos de dados
# O texto será uma string.
def rotacionar_direita(texto: str, n: int) -> str:
    '''
    Rotacionar *texto* a direita *n* caracteres, movendo os ultimos *n* caracteres para o início de *texto*.
    *n* deve ser positivo.

    Exemplos:
    >>> ('Lucas',2)
    'asLuc'
    >>> ('Bom dia',3)
    'diaBom'
    >>> ('',3)
    ''
    >>> ('Casa',0)
    'Casa'
    '''
    return texto[(len(texto) - n):] + texto[:(len(texto) - n)]
