# Análise
# Converte uma data no formato dia/mês/ano para o formato ano/mês/dia

# Tipos de dados
# Dia, mês e ano serão strings.

def diamesano_para_anomesdia(dia, mes, ano: str) -> str:
    '''
    Converter uma data no formato dia/mês/ano para o formato ano/mês/dia. O dia e o mês serão no formato de dezenas(XX), enquanto o ano será no
formato de milésimos(XXXX).
    Exemplos:
    >>> ('24','01','2005')
    '2005/01/24'
    >>> ('04','09','2023')
    '2023/09/04'
    '''
    return ano + '/' + mes + '/' + dia