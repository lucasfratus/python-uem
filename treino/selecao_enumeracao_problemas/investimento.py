# Analise
# Calcula quanto um investimento irá render no perído de um ano.
# Para valores até 2000,00 reais, a taxa de correção é de 10%.
# Para valores entre 2000,00 e 5000 reais, a taxa de correção é de 12%.
# Para valores acima de 5000,00 reais, a taxa de correção de é de 13%.

# Tipos de dados
# O valor aplicado sera representado em reais e será um float positivo.

def investimento(valor_aplicado: float) -> float:
    '''
    Calcula quanto *valor_aplicado* irá render em um ano, dependendo da quantidade desse valor.
    Se *valor_aplicado* <= 2000,00, o rendimento será de 10%
    Se *valor_aplicado* > 2000,00 e *valor_aplicado* < 5000,00, o rendimento será de 12%.
    Se *valor_aplicado* >= 5000,00 o rendimento será de 13%.
    *valor_aplicado* deve ser igual ou maior a zero.
    Exemplos
    >>> investimento(1900.00)
    190.00
    >>> investimento(3000.00)
    360.00
    >>> investimento(6000.00)
    780.00
    '''
    assert valor_aplicado >= 0
    if valor_aplicado <= 2000.00:
        rendimento = valor_aplicado * 10/100
    elif valor_aplicado > 2000.00 and valor_aplicado < 5000.00:
        rendimento = valor_aplicado * 12/100
    else: # valor_aplicado >= 5000.00
        rendimento = valor_aplicado * 13/100
    return rendimento

def investimento_2(valor_aplicado: float) -> float: 
    '''
    Calcula quanto *valor_aplicado* irá render em dois anos, dependendo da quantidade desse valor.
    Se *valor_aplicado* <= 2000,00, o rendimento será de 10%
    Se *valor_aplicado* > 2000,00 e *valor_aplicado* < 5000,00, o rendimento será de 12%.
    Se *valor_aplicado* >= 5000,00 o rendimento será de 13%.
    *valor_aplicado* deve ser igual ou maior a zero.
    Exemplo
    >>> investimento_2(1900.00)
    380.00
    >>> investimento_2(3000.00)
    720.00
    >>> investimento_2(6000.00)
    1560.00
    '''
    return 2 * investimento(valor_aplicado)
