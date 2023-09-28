# Análise
# Move os últimos caracteres de um texto para as primeiras posições do mesmo texto.
# A quantidade de caracteres movidos será fornecida pelo usuário.

# Tipos de dados 
# O texto será uma string.
# A quantidade de caracteres movidos será um número inteiro positivo

def rotacionar_string(texto: str, n: int) -> str:
    '''
    Rotaciona um texto *n* posições para a direita, medindo a quantidade de caracteres de um texto e considerando *n* a
    quantidade de últimos caracteres a serem movidos para as *n* primeiras posições do texto.

    Exemplos:
    >>> rotacionar_string('Marcelo',5)
    'rceloMa'
    >>> rotacionar_string('Lucas',3)
    'casLu'
    '''
    return texto[-n:] + texto[:-n]
