# Analise
# Encontra as posições de todas as ocorrências de um nome em uma lista de nomes

# Tipos de dados
# A lista de nomes será composta de strings

def ocorrencia(nome : str, lst: list[str]) -> list[int]:
    '''
    Encontra os indice de todas as ocorrências de uma string em * lst*, gerando uma nova lista composta por essas
    indices. *lst* não pode ser vazia.
    Exemplo
    >>> ocorrencia('casa',['casa','porta','casa']) 
    [0,2]
    >>> ocorrencia('casa',['casa'])
    [0]
    >>> ocorrencia('porta',['casa'])
    []
    '''
    ocorrencia_nome = []
    for x in range(len(lst)):
        if lst[x] == nome:
            ocorrencia_nome.append(x)
    return ocorrencia_nome