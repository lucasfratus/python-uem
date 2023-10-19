# Analise
# Encontra todas as posições de ocorrencias de um nome em uma lista de strings
# Tipos de dados
# A lista será composta de strings.

def encontra_posicoes(lst: list[str], nome: str) -> list[int]:
    '''
    Encontra todas as posições de ocorrencias de *nome* em *lst*. *lst* não pode ser vazia. Caso não encontre,
    devolve uma lista de inteiros vazia.
    Exemplos:
    >>> encontra_posicoes(['Pedro','Leandro','Cesar','João','Cesar'], 'Lucas')
    []
    >>> encontra_posicoes(['Pedro','Leandro','Cesar','João','Cesar'], 'Pedro')
    [0]
    >>> encontra_posicoes(['Pedro','Leandro','Cesar','João','Cesar'], 'Cesar')
    [2, 4]
    '''
    i = 0
    lista_posicoes = []
    while i < len(lst):
        if lst[i] == nome:
            lista_posicoes.append(i)
        i = i + 1
    return lista_posicoes
