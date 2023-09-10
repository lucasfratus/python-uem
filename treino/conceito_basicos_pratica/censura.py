# Analise
# Censura uma certa quantidade de letras do início uma frase, trocando-as por 'x'.

# Tipos de dados
# A frase será uma string.
# A quantidade de letras censuradas será um numero inteiro positivo.

def main():
    # entrada
    frase: str = input('Digite a frase que deseja inserir uma censura no início: ')
    n: int = int(input('Digite o número de letras que deseja censurar: '))

    # processamento
    censurado: str = censura(frase,n)

    # saida
    print(censurado)

def censura(frase: str, n: int) -> str:
    '''
    Censurar uma quantidade *n* inteira e positiva de letras do início de uma *frase*. A *frase* não pode ser um string vazia.
    Exemplos
    >>> ('Droga de lanche!',5)
    'xxxxx de lanche!'
    >>> ('porcaria de livro!',8)
    'xxxxxxxx de livro!'
    '''
    return n * 'x' + frase[n:]
main()