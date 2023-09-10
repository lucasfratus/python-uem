# Análise
# Acrescenta uma certa quantidade, dada em forma de porcentagem, a um valor positivo.

# Tipos de Dados
# Os valores serão números inteiros positivos.

def main():
    # entrada
    valor: int = int(input('Insira um valor inteiro positivo: '))
    porcentagem: int = int(input('Insira uma porcentagem que deseja adicionar ao valor anterior: '))

    # processamento
    valor_final: int = aumenta(valor,porcentagem)

    # saida
    print('A soma do valor',valor,'com',porcentagem,'% é',valor_final)

def aumenta(valor, porcentagem: int) -> int:
    '''
    Adicionar uma *porcentagem* de determinado *valor* a ele mesmo, sendo ambos números inteiros positivos.
    Exemplos:
    >>> (10,10)
    11
    >>> (100,1)
    101
    >>> (1000,3)
    1030
    '''
    return valor + (valor * porcentagem/100)
main()