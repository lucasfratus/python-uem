def main():
    #Entrada
    n: int = int(input('Escreva um número real qualquer:'))

    #Processamento
    npap: int = produto_anterior_posterior(n)

    #Saida
    print('O produto entre ',n,', ',n-1,' e ',n+1,' é ',npap,sep='')

def produto_anterior_posterior(n: int) -> int:
    return n * (n-1) * (n+1)

main()
