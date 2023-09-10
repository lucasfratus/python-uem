# Analise
# Conta quantas vezes o valor minímo de uma lista de inteiros não vazia aparece na lista.

# Tipos de dados
# A lista será composta de inteiros.

def valor_minimo(lst: list[int]) -> int:
    '''
    Conta quantas vezes o valor minimo de *lst* aparece na lista. *lst* nao pode ser vazia.
    Exemplos
    >>> valor_minimo([1,3,4,1])
    2
    >>> valor_minimo([2,3,4,3])
    1
    >>> valor_minimo([1])
    1
    '''
    valor_minimo = lst[0]
    contagem = 0

    
    # Definindo valor_minimo
    for n in lst:
        if n < valor_minimo:
            valor_minimo = n
    # Definindo contagem de minimos
    for n in lst:
        if n == valor_minimo:
            contagem = contagem + 1
    return contagem

def valor_minimo2(lst: list[int]) -> int:
    '''
    Conta quantas vezes o valor minimo de *lst* aparece na lista. *lst* nao pode ser vazia.
    Exemplos
    >>> valor_minimo2([1,3,4,1])
    2
    >>> valor_minimo2([2,3,4,3])
    1
    >>> valor_minimo2([1])
    1
    '''
    valor_minimo = lst[0]
    contagem = 0

    for n in lst:
        if n == valor_minimo:
            contagem = contagem + 1
        elif n < valor_minimo:
            contagem = 1
            valor_minimo = n
    return contagem