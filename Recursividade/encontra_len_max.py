# Análise
# Encontra a string com maior tamanho de uma lista de strings a partir de um certo indice, por meio de função recursiva.
# Tipos de dados
# A lista será composta por strings.
# O indice será um número inteiro, entre 0 e o tamanho da lista strings.
# Maior será uma string vazia

def encontra_len_max(lst: list[str], i: int, maior: '') -> str:
    '''
    Encontra a string com maior tamanho de *lst* por meio de recursividade. Caso haja um empate, a lista que aparece por ultimo será a string devolvida.
    *maior* será sempre uma string vazia
    0 <= *i* <= len(lst)
    Exemplos:
    >>> encontra_len_max([''], 0, '')
    ''
    >>> encontra_len_max(['','as','foi'], 0, '')
    'foi'
    >>> encontra_len_max(['a','b','c'], 0, '')
    'c'
    >>> encontra_len_max(['','baas','foi'], 0, '')
    'baas'
    '''
    if i == len(lst):
        return maior
    else:
        if len(lst[i]) >= len(maior):
            maior = lst[i]
            maior = encontra_len_max(lst, i+1, maior)
    return maior
