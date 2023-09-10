# Analise
# Verifica se um texto inicia e termina com espaços extras.

# Tipos de dados
# O texto será uma string.

def sem_espacos_extras(texto: str) -> bool:
    '''
    Produz True se *texto* não possuir espaços no começo e no final.
    Caso contrário, produz False.
    Exemplos:
    >>> sem_espacos_extras('Bom dia')
    True
    >>> sem_espacos_extras(' Bom dia')
    False
    >>> sem_espacos_extras('Bom dia ')
    False
    >>> sem_espacos_extras(' Bom dia ')
    False
    '''
    return texto == '' or (texto[0] != ' ' and texto[(len(texto) - 1)] != ' ')

