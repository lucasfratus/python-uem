# Analise
# Tranforma a primeira letra da frase em maiúscula.

# Tipos de dados
# A frase será uma string.

def main():
    # entrada
    frase: str = input('Digite a frase que deseja converter a primeira dela em maiúscula: ')
    # processamento
    maiuscula: str = primeira_maiuscula(frase)
    # saída
    print(maiuscula)

def primeira_maiuscula(frase: str) -> str:
    '''
    Transformar a primeira letra de *frase* em letra maiúscula.
    Exemplos:
    >>> ('amo sorvete')
    'Amo sorvete'
    >>> ('fabio')
    'Fabio'
    >>> ('Minha casa')
    'Minha casa'
    '''
    return frase[0].upper() + frase[1:]

main()