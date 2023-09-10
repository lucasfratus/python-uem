# Analise
# Calcula a unidade, dezena e centena de um número inteiro.

# Tipos de dados
# O número será um inteiro positivo.

def main():
    # entrada
    n: int = int(input('Insira o número que deseja calcular a unidade, dezena e centena:'))

    # processamento
    uni: int = unidade(n)
    dez: int = dezena(n)
    cent: int = centena(n)

    # saida
    print('unidade:',uni)
    print('dezena:',dez)
    print('centena:',cent)

def unidade(n: int) -> int:
    '''
    Calcular a unidade de um número inteiro positivo.
    Exemplos
    >>> unidade(15)
    5
    >>> unidade(201)
    1
    >>> unidade(1124)
    4
    '''
    return n % 10
    
def dezena(n:int) -> int:
    '''
    Calcular a dezena de um número inteiro positivo.
    Exemplos
    >>> unidade(15)
    1
    >>> unidade(120)
    2
    >>> unidade(2130)
    3
    '''
    return n // 10 % 10
    
def centena(n:int) -> int:
    '''
    Calcular a centena de um número inteiro positivo.
    >>> centena(15)
    0
    >>> centena(120)
    1
    >>> centena(1245)
    1
    '''
    return n // 100 % 10
    
main()