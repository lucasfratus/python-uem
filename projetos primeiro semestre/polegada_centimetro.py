def main():
    #input
    polegada: float = float(input('Digite a medida, em polegadas, que você deseja converter para centímetros:'))

    #processamento
    centimetro: float = polegada_centimetro(polegada)

    #saida
    print(polegada,'polegada(s) convertido para centímetros é',centimetro)

def polegada_centimetro(polegada: float) -> float:
    return polegada * 2.54

main()