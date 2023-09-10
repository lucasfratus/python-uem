# Analise
# Verifica se um nome é mediano, levando em conta que, se possuir no máximo 3 letras é um nome curto e se possuir mais que 8 é longo.

# Tipos de dados
# O nome será uma string.

def nome_mediano(nome: str) -> bool:
    return 3 < len(nome) < 9
