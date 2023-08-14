def qualificacao(num_questoes: int, num_acertos:int, faltas: float) -> str:
    '''
    Indica, por meio da analise do *aproveitamento*(razao entre o numero de acertos e numero de questoes) e das *faltas*, se houve 
    a aprovaçao, reprovaçao ou uma possibilidade de nova tentativa do aluno.
    
    Exemplos
    >>> qualificacao(10,6,0.10)
    'aprovado'
    >>> qualificacao(10,3,0.30)
    'reprovado'
    >>> qualificacao(10,7,0.40)
    'reprovado'
    
    ''' 
    aproveitamento = num_acertos / num_questoes
    if aproveitamento < 0.3 or faltas > 0.25:
        resultado = 'reprovado'
    elif aproveitamento < 0.6:
        resultado = 'nova tentativa'
    else:
        resultado = 'aprovado'
    return resultado