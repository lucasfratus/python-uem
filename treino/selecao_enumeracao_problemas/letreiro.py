# Analise
# Determina os caracteres que aparecerão em um letreiro com um certo
# número de caracteres em determinado momento. A mensagem sempre terá mais
# caracteres que o letreiro.

# Tipos de dados
# A mensagem será uma string.
# O número de caracteres do letreiro será um inteiro positivo
# O momento será representado em segundos e será um inteiro positivo.

def letreiro(mensagem: str, n_letreiro: int, momento: int) -> str:
    '''
    Gera uma nova string que aparecera em um letreiro com base na *mensagem* , a quantidade *n_letreiro* de caracteres do letreiro 
    e o *momento*.
    Assuma que *n_letreiro* é menor que a quantidade de caracteres de *mensagem*.
    Quando *mensagem* for mostrada completamente, ela começará a ser exibida novamente.
    Exemplo
    >>> letreiro('Venha comprar aqui!', 5, 0)
    'Venha'
    >>> letreiro('Venha comprar aqui!', 5 ,2)
    'nha C'
    >>> letreiro('Venha comprar aqui!', 5, 15)
    'ui! V'
    '''
    
    if momento > len(mensagem) - n_letreiro:
        final = mensagem[momento : n_letreiro + momento] + mensagem[(momento % len(mensagem)) + n_letreiro:momento - (len(mensagem) - n_letreiro)]
    else:
        final = mensagem[momento : n_letreiro + momento]   
    return final
