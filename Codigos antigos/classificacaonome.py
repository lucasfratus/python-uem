# Analise
# Classifica um nome em curto, médio e longo de acordo com a quantidade de letras.

# Tipos de dados
# O texto fornecido pelo usuário será uma string.

def tamanho_nome(nome: str) -> str:
    if len(nome) <= 4:
        tamanho = 'curto'
    elif len(nome) > 4 and len(nome) < 8:
        tamanho = 'mediano'
    else:
        tamanho = 'longo'
    
    return tamanho