# Analise
# Verifica se o nome inserido é Paula, assumindo que a entrada não possui espaços no inicio e no final.

# Tipos de dados
# O nome é uma string.
def main():
    # entrada
    nome: str = input('Insira o seu nome')

    # processamento
    verificacao: bool = nome_paula(nome)

    # saida
    print('É',verificacao,'que seu nome é Paula')

def nome_paula(nome: str) -> bool:
    '''
    Verificar se o *nome* é igual a Paula, não contendo espaços no início e nem no final.
    Exemplos
    >>> nome_paula('Fabio')
    False
    >>> nome_paula('Pedro')
    False
    >>> nome_paula('Paula')
    True
    '''
    return nome == 'Paula'
main()