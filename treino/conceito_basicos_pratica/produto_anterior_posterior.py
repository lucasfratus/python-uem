# Análise
# Calcula o produto entre um número, o seu antecessor e o seu posterior.

# Tipos de Dados
# Os números serão inteiros.

def main():
    # entrada
    n: int = int(input('Insira um número: '))

    # processamento
    produto_n: int = produto_anterior_posterior(n)

    # saida
    print('O produto entre ',n,', ', n - 1, ' e ', n + 1, ' é ', produto_n, sep='')

def produto_anterior_posterior(n: int) -> int:
    '''
    Calcular o produto entre *n*, seu antecessor(*n* - 1) e seu posterior(*n* + 1).
    Exemplos
    >>> (2)
    6
    >>> (0)
    0
    >>> (3)
    24
    '''
    return n * (n - 1) * (n + 1)

main()