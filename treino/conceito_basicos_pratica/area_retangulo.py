# Análise
# Calcula a área de um retângulo recebendo a largura e altura da figura.

# Tipos de Dados
# A largura será um ponto flutuante positivo.
# A altura será um ponto flutuante positivo.

def main():
    # entrada
    largura: float = float(input('Qual a largura do retângulo?'))
    altura: float = float(input('Qual a altura do retângulo?'))

    #processamento
    a: float = area(largura,altura)

    #saida
    print('A área de um retângulo de largura',largura,'e de altura',altura,'é',a,'centímetros quadrados.')

def area(largura: float, altura: float) -> float:
    '''
    Calcula a área de um retângulo através do produto entre *largura* e *altura*. Os valores de *largura* e *altura* devem ser maiores 
    e diferentes de zero.
    >>> (12.0,3.0)
    36.0
    >>> (10.5,2.0)
    21.0
    >>> (11.0,3.0)
    33.0
    '''
    return largura * altura
main()