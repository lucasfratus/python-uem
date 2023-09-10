# Analise
# Verifica se o último nome(sobrenome) é Silva.

# Tipos de dados
# O nome será uma string.
def main():
    # entrada
    sn: str = input('Insira seu nome e sobrenome: ')

    # processamento
    verificacao: bool = sobrenome(sn)

    # saida
    print('É',verificacao,'que o seu sobrenome é Silva!')
def sobrenome(sn:str) -> bool:
    '''
    Verificar se o último nome(sobrenome) é Silva. A string de entrada não possui espaços no seu início nem no seu final e contém pelo menos um espaço em branco.
    Exemplos
    >>> sobrenome('Pedro Silva')
    True
    >>> sobrenome('Sonia Castro')
    False
    >>> sobrenome('Silva Santos')
    False
    '''
    return sn[-5:] == 'Silva' 

main()