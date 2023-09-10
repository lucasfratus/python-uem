# Análise
# Adiciona uma certa quantidade de pontos de exclamação no final de um texto.

# Tipos de dados
# O número de exclamações será um inteiro positivo.
# O texto será uma string.

def main():
    # entrada
    texto: str = input('Digite uma frase que deseja adicionar pontos de exclamação no final: ')
    n: int = int(input('Insira o número de exclamações que deseja adicionar ao texto anterior: '))

    # processamento
    texto_n: str = exclamacao(texto,n)

    # saida
    print(texto_n)
def exclamacao(texto: str, n: int) -> str:
    '''
    Adicionar ao final de *texto* um valor *n* inteiro e positivo de exclamações.
    Exemplos
    >>> ('Adoro sorvete',1)
    'Adoro sorvete!'
    >>> ('Olá',5)
    'Olá!!!!!'
    >>> ('',1)
    '!'
    '''
    return texto + n * '!'
main()
