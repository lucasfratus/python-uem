# Análise
# Calcular a hipotenusa a partir dos valores dos catetos de um triângulo.

# Tipos de dados
# As medidas dos lados do triângulo serão números flutuantes positivos.

def hipotenusa(cateto1, cateto2: float) -> float:
    '''
    Calcula o valor da hipotenusa de um triângulo através de seus catetos. A hipotenusa de um triângulo é calculada através da raiz quadrada
    da soma dos quadrados dos catetos. O valor da hipotenusa precisa ser maior que zero e menor que a soma dos catetos.
    Exemplos:
    >>> (12,5)
    13
    >>> (3,4)
    5
    >>> (9,16)
    25
    '''
    return (cateto1 ** 2  + cateto2 ** 2)  ** 0.5
