# Analise
# Transforma uma string em outra com um número dado de caracteres. Se essa string possui um número de caracteres que é maior o número dado,
# os excedentes serão removidos. Se a string possuir uma quantidade de caracteres menor que o número dado,
# espaços em branco serão adicionados.

# Tipos de dados
# O texto será uma string.
# O número será um inteiro positivo.

def caracteres_string(texto: str, n: int) -> str:
    '''
    Gera uma string a partir de *texto*, que possui um número *n* informado de caracteres.
    *n* deve ser um inteiro positivo e *texto* não pode ser uma string vazia.
    >>> caracteres_string('Hoje o dia está bonito',4)
    'Hoje'
    >>> caracteres_string('Sol',5)
    'Sol  '
    >>> caracteres_string('Porta',5)
    'Porta'
    '''
    assert texto != ''
    assert n >= 0
    if n > len(texto) :
        string_n = texto + (n - len(texto)) * ' '
    elif n == 0:
        string_n = ''
    else:
        string_n = texto[0:n]
    return string_n



