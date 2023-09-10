# Analise
# Verifica se uma pessoa é isenta da tarifa de transporte público. Para ser isenta, uma pessoa deve ter menos de 18 ou 65 ou mais.

# Tipos de dados
# A idade será dada em anos e será um número inteiro positivo.

def isento_tarifa(idade: int) -> bool:
    '''
    Produzir True se é isento da tarifa de ônibus. Para ser isento, a idade precisa ser menor que 18 anos ou igual ou maior que 65.
    Produz False caso contrário.
    Exemplos
    >>> isento_tarifa(17)
    True
    >>> isento_tarifa(18)
    False
    >>> isento_tarifa(25)
    False
    >>> isento_tarifa(65)
    True
    >>> isento_tarifa(70)
    True
    '''
    return idade < 18 or idade >= 65
    
