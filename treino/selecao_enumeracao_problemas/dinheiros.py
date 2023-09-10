# Analise
# Calcula quanto de imposto cada cidadão deve pagar de acordo com sua renda
# Quem recebe até 1000 dinheiros paga 5% de imposto
# Quem recebe entre 1000 e 5000 dinheiros paga 5% sobre 1000 dinheiros e 10% sobre o que passar de 1000.
# Quem recebe mais de 5000 dinheiros paga 5% sobre 1000 dinheiros, 10% sobre 4000 dinheiros e 20% sobre o que passar de 5000.

# Tipos de dados
# A renda será representada em dinheiros e em números inteiros positivos

def imposto(renda: int) -> float:
    '''
    Calcula quanto de imposto será pago levando em conta *renda*.
    Caso *renda* <= 1000, o imposto será 5% da renda.
    Caso *renda* > 1000 e *renda* < 5000, o imposto será 5% sobre os primeiros 1000 dinheiros e 10% sobre o que passar de 1000.
    Caso *renda* >= 5000, o imposto será 5% sobre os primeiros 1000 dinheiros,10 % sobre os 4000 e 20% sobre o que passar de 5000
    Exemplos
    >>> imposto(500)
    25.0
    >>> imposto(2000)
    150.0
    >>> imposto(6000)
    750.0
    '''
    assert renda >= 0
    if renda <= 1000:
        imposto_renda = renda * 5/100
    elif renda > 1000 and renda < 5000:
        imposto_renda = (1000 * 5/100) + (renda - 1000) * 10/100
    else: # renda >= 5000
        imposto_renda = (1000 * 5/100) + (renda - 1000) * 10/100 + (renda - 5000 ) * 20/100
    return imposto_renda