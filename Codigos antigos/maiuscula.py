def main():
    #entrada
    frase: str = input('Digite a frase que deseja que a primeira letra fique maiúscula: ')

    #processamento
    fm: str = maiuscula(frase)

    #saida
    print('A frase com a primeira letra maiúscula fica:','\n',fm)

def maiuscula(frase:str) -> str:
    return frase[0].upper() + frase[1:]

main()