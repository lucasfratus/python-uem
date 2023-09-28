def main():
    #input
    b: int= int(input('Insira o valor de um cateto do triângulo:'))
    c: int= int(input('Insira o valor do outro cateto do triângulo:'))
    
    #processamento
    r: int = hipotenusa(b,c)

    #output
    print('O valor da hipotenusa de um triângulo com catetos de',b,'e',c,'é',r)


def hipotenusa(b,c: int) -> int:
    return (b ** 2 + c ** 2) ** (1/2)

main()