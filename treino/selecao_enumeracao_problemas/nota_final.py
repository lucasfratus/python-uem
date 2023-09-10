from enum import Enum, auto
# Analise
# Indica a situação de um aluno de acordo com a nota final. A nota final é calculada pela media de 4 avaliações que valem de 0 a 10.
# Se a nota final é maior ou igual a 7, o aluno é aprovado
# Se a nota final é menor que 4, é reprovado.
# Se a nota final é maior igual a 4 e menor que 7, o aluno fica de exame.

# Tipos de dados
# As notas das avaliações serão floats positivos

class Situacao(Enum):
    '''
    Situação do aluno
    '''
    APROVADO = auto()
    REPROVADO = auto()
    EXAME = auto()

def situacao_nota(nota1, nota2, nota3, nota4: float) -> Situacao:
    '''
    Indica a situação de um aluno de acordo com sua nota final. A nota final é calculada através da média de *nota1*, *nota2*, *nota3* e
    *nota4*. 
    Se nota final é >= 7, o aluno é aprovado.
    Se nota final é < 4, o aluno é reprovado.
    Se nota final é >= 4 e < 7, o aluno fica de exame.
    Exemplo
    >>> situacao_nota(4,6,8,6).name
    'EXAME'
    >>> situacao_nota(7,7,7,7).name
    'APROVADO'
    >>> situacao_nota(3,4,2,1).name
    'REPROVADO'
    '''
    nota_final = (nota1 + nota2 + nota3 + nota4) / 4
    if nota_final >= 7:
        situacao_final = Situacao.APROVADO
    elif nota_final >= 4 and nota_final < 7:
        situacao_final = Situacao.EXAME
    else: # nota_final < 4
        situacao_final = Situacao.REPROVADO
    return situacao_final


