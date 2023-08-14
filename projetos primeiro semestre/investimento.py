# Analise
# Calcula quanto uma investimento ira render ate o fim de um ano. Se o investimento for ate 2000 reais,
# a taxa de correçao é de 10%. Caso o valor for entre 2000 e 5000 a taxa é de 12%. Para valores maiores,
# é de 13%.

# Tipos de Dados
# O valor investido é dado em números flutuantes positivos.
# O valor final é retornado em números flutuantes inteiros.


def investimento(valor_aplicado: float) -> float:
    '''
    Calcular o rendimento de um *valor_aplicado* em um investimento em um ano. Se o *valor_aplicado* for ate 2000
    reais, o rendimento é de 10% do valor inicial. Se for entre 2000 e 5000, é 12%.E para valores maiores
    ou iguais a 5000, é de 13%.

    Exemplos
    >>> investimento(1950.00)
    195.0
    >>> investimento(2000.00)
    260.0
    >>> investimento(2500.0)
    300.0
    >>> investimento(5100.0)
    663.0
    '''
    if valor_aplicado < 2000.00:
        valor_retornado = valor_aplicado * 10/100

    elif valor_aplicado > 2000.00 and valor_aplicado < 5000.00:
        valor_retornado = valor_aplicado * 12/100

    else:
        valor_retornado = valor_aplicado * 13/100
    
    return valor_retornado