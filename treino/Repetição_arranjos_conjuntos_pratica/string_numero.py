# Analise
# Cria uma lista de números a partir de uma lista de strings, convertendo cada uma das strings em números.

# Tipos de dados
# Os elementos da lista de entrada serão strings.

def string_numero(lst: list[str]) -> list[int]:
    '''
    Cria uma lista de números inteiros a partir de *lst*, convertendo cada uma das strings de *lst* em números. Nenhum elemento de *lst*
    pode ser uma string vazia. Todos os elementos de *lst* devem ser números inteiros em forma de string.
    Exemplos
    >>> string_numero(['1','2','3'])
    [1,2,3]
    >>> string_numero(['10','-7'])
    [10,-7]
    '''
    lista = []
    for s in lst:
        lista.append(int(s))
    return lista