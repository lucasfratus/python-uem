def dma_para_amd(data: str) -> str:
    '''
    Transforma *data*, que deve estar no formato 'dia/mes/ano', para o formato 'ano/mes/dia'.
    'Dia' e 'Mes' possui dois digitos e 'ano' possui quatro.
    Exemplos
    >>> dma_para_amd('24/01/2005')
    '2005/01/24'
    >>> dma_para_amd('01/01/2001')
    '2001/01/01'
    '''
    assert len(data) == 10
    return data[6:] + '/' + data[3:5] + '/' + data[:2]
