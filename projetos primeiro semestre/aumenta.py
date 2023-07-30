def main():
    #entrada
    valor: float = float(input('Insira um valor:'))
    porcentagem: float = float(input('Insira uma porcentagem que deseja somar com o valor anterior:'))

    #processamento
    vp: int = aumenta(valor,porcentagem)

    #saida
    print('A soma entre o valor ',valor,' e ',porcentagem,'% do mesmo é ',vp,sep='')

def aumenta(valor,porcentagem: float) -> float:
    return valor + valor * porcentagem/100

main()
