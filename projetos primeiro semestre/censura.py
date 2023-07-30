def main():
    #entrada
    frase: str = input('Digite uma frase que contém uma palavra que deseja censurar:')
    n: int = int(input('Digite a quantidade de letras que a palavra que você deseja censurar possui:'))

    #processamento
    censorship: str = censura(frase,n)

    #saida
    print('A frase censurada é:','\n',censorship)

def censura(frase: str, n: int) -> str:
    return '#' * n + frase[n:]

main()