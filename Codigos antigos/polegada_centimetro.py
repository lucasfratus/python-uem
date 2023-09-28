def main():
    #input
    polegada: float = float(input('Digite a medida, em polegadas, que você deseja converter para centímetros:'))

    #processamento
    centimetro: float = polegada_centimetro(polegada)

    #saida
    print(polegada,'polegada(s) convertido para centímetros é',centimetro)

def polegada_centimetro(polegada: float) -> float:
    '''
    Converte a medida em polegadas em centímetros.
    
    Exemplos
    >>> polegada_centimetro(1)
    2.54
    >>> polegada_centimetro(2)
    5.08
    >>> polegada_centimetro(3)
    7.62
    '''
    return polegada * 2.54

main()