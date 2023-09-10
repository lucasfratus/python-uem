# Análise
# Zera a dezena e unidade de um número natural.

# Tipos de dados
# O número será um inteiro positivo.
def main():
    # entrada
    n: int = int(input('Digite um número que você deseja zerar a dezena e a unidade: '))

    # processamento
    zerado: int = zera_dezena_e_unidade(n)

    # saida
    print('O número',n,'com a dezena e unidade zeradas é', zerado)

def zera_dezena_e_unidade(n: int) -> int:
    '''
    Zerar a dezena e unidade de um número inteiro positivo *n*.
    Exemplos:
    >>> (5)
    0
    >>> (50)
    0
    >>> (153)
    100
    >>> (1243)
    1200
    '''
    return n // 100 * 100
main()
