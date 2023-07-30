def main():
    #entrada
    dia: str = str(input('Insira o dia do mês:'))
    mes: str = str(input('Insira o mês:'))
    ano: str = str(input('Insira o ano:'))
    
    #processamento
    data1: str = data_amd(dia,mes,ano)

    #saida
    print('A data convertida para o formato "ano/mês/dia" é',data1,)

def data_amd(dia,mes,ano: str) -> str:
    return ano + '/' + mes + '/' + dia

main()