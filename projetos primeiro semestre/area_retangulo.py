def main():
    #entrada
    b: int = int(input('Qual a medida da base do retângulo?'))
    h: int = int(input('Qual a medida da altura do retângulo?'))
    
    #processamento
    a: int = area(b,h)

    #saida
    print('A área de um retângulo de base',b,'e altura',h,'é',a)

def area(b,h:int) -> int:
    return b * h

main()
