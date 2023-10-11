# Analise
# Determina a menor quantidade de elementos de uma lista que precisam ser somados(a partir do inicio da lista)
# para que a soma seja maior que um dado valor. Se não atingir a soma deseja, devolve -1.

# Tipos de Dados
# A lista será composta de números inteiros.
# O valor desejado é um inteiro positivo.

def determina_menor_quantidade(lst: list[int], valor_desejado: int) -> int:
    '''
    Determina a menor quantidade de elementos de *lst* que precisam ser somado para que seja maior que *valor_dese
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
    maior = 0
    indice_maior = 0
    lista_definitiva = []
    for x in range(len(lst)):
        for y in range(x, len(lst)):
            if lst[x] > maior and lst[x] > lst[y]:
                maior = lst[x]
                lista_definitiva.append(maior)
                indice_maior = x 
                lst = lst[:indice_maior] + lst[indice_maior+1:]
            else
    
    # função
    i = 0
    soma = 0
    quantidade = 0
    while i < len(lista_definitiva):
        if soma <= valor_desejado:
            soma = soma + lista_definitiva[i]
            quantidade = quantidade + 1
        if soma <= valor_desejado and i == len(lista_definitiva) - 1:
            quantidade = -1
        i = i + 1
    return quantidade





