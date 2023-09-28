def main():
    #entrada
    frase: str = input('Digite uma frase que você deseja adicionar exclamações:')
    exc: int = int(input('Qual o número de exclamações que você deseja adicionar?'))

    #processamento
    fe : str =  exclamacao(frase,exc)

    #saida
    print('A frase',frase,'com',exc,'exclamações fica:','\n',fe)

def exclamacao(frase:str, exc: int) -> str:
    return frase + exc * '!'

main()

    