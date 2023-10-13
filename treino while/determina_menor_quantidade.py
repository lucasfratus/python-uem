# Analise
# Determina a menor quantidade de elementos de uma lista que precisam ser somados(a partir do inicio da lista)
# para que a soma seja maior que um dado valor. Se não atingir a soma deseja, devolve -1.

# Tipos de Dados
# A lista será composta de números inteiros.
# O valor desejado é um inteiro positivo.

def determina_menor_quantidade(lst: list[int], valor_desejado: int) -> int:
    '''
    Determina a menor quantidade de elementos de *lst* que precisam ser somados para que seja maior que *valor_dese
    jado*. Caso não atingir, devolve -1.
    Exemplos:
    >>> determina_menor_quantidade([],7)
    -1
    >>> determina_menor_quantidade([2,3,5,7,8],2)
    1
    >>> determina_menor_quantidade([1,2,4],7)
    -1
    >>> determina_menor_quantidade([7,8],1)
    1
    '''
    # ordena a lista
    i = 0
    lista_definitiva = []
    while i < len(lst):
        maior = lst[0]
        for x in range(len(lst)):
            if lst[x] > maior:
                maior = lst[x]
                indice_maior = x
        i = i+1
        lista_definitiva.append(maior)
        lst = lst[:indice_maior] + lst[indice_maior + 1:]
    i2 = 0 
    soma = 0
    while i2 < len(lista_definitiva) and soma < valor_desejado:
        soma = soma + lista_definitiva[i2]
        i2 = i2 + 1
    if soma < valor_desejado:
        i2 = -1
    return i2

