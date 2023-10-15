# Analise
# Cria uma lista de inteiros a partir de uma lista de strings, convertendo cada string em um número

# Tipos de dados
# A lista será composta por strings.

def converte_str_int(lst: list[str]) -> list[int]:
    '''
    Cria uma nova lista a partir de *lst*, convertendo cada string em um número.
    *lst* não pode ser vazia
    Exemplos:
    >>> converte_str_int(['1','2','3'])
    [1,2,3]
    >>> converte_str_int(['-1','0','400'])
    [-1,0,400]
    '''
    lista_convertida = []
    for x in lst:
        lista_convertida.append(int(x))
    return lista_convertida