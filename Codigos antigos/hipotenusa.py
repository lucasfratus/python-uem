def main():
    #input
    b: int= int(input('Insira o valor de um cateto do triângulo:'))
    c: int= int(input('Insira o valor do outro cateto do triângulo:'))
    
    #processamento
    r: int = b ** 2 + c ** 2
    pit: int = hipotenusa(r)

    #output
    print('O valor da hipotenusa de um triângulo com catetos de',b,'e',c,'é',pit)


def hipotenusa(r: int) -> int:
    #import do modulo math
    import math

    #função
    return math.sqrt(r)

main()