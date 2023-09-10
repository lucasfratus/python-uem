import math
# Analise
# Recebe as notas finais de um aluno e verifica se ele receberá a Laurea Academica. A laurea academica é recebida se o aluno possui
# mais do que 2/3 de suas notas finais maiores que 9.0. As notas vão de 0 a 10;0

# Tipos de dados
# A lista de notas finais será representada por floats positivos de 0 a 10.0,

def laurea(lst: list[float]) -> bool:
    '''
    Verifica se um aluno receberá a laurea academica através da *lst* de notas finais. 
    Se pelo menos 2/3 das notas finais forem maior que 9.0, produz True.
    Caso contrário, produz False
    Exemplos
    >>> laurea([9.5,9.5,8.5])
    True
    >>> laurea([9.0,9.7])
    True
    >>> laurea([8.0,8.5,9.3])
    False
    '''
    assert 0 != len(lst)
    lista_90 = []
    for n in lst:
        if n >= 9.0:
            lista_90.append(n)
    if len(lista_90) < math.ceil(2/3 * len(lst)):
        verificacao = False
    else:
        verificacao = True
    return verificacao

