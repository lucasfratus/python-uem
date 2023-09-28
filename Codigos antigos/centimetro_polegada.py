def main():
    #entrada
    centimetro: float = float(input('Digite a medida, em centímetros, que você deseja converter para polegadas:'))

    #processamento
    polegada: float = centimetro_polegada(centimetro)

    #saida
    print(centimetro,'centímetro(s) convertido para polegadas é',polegada)

def centimetro_polegada(centimetro: float) -> float:
    return (centimetro * 1/2.57)

main()