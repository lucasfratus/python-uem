from dataclasses import dataclass
# Analise
# Determine o candidato melhor classificado em um concurso. Nesse concurso, a classificação é feita por pontos que vão de 0 a 100. No caso
# de empate, o candidato com menor número de inscrição é classificado.

# Tipos de dados.
# O número de inscrição e a pontuação do candidato estarão em uma estrutura.
# A pontuação é um inteiro positivo de 0 a 100
# O número de inscrição será assumido como um inteiro positivo diferente de 0

@dataclass
class Candidato:
    '''
    Desempenho  e número de inscrição do candidato.
    '''
    pontuacao: int
    inscricao: int

def classificacao(a: Candidato, b: Candidato) -> Candidato:
    '''
    Determina qual candidato entre *a* e *b* foi classificado. A classificação é determinada através do maior número de pontos porém,
    quando há um empate, o classificado é determinado através do menor número de inscrição.
    Exemplos
    >>> classificacao(Candidato(9,120),Candidato(8,100))
    a
    >>> classificacao(Candidato(5,100),Candidato(6,132))
    b
    >>> classificacao(Candidato(8,120),Candidato(8,112))
    b
    >>> classificacao(Candidato(9,109),Candidato(9,134))
    a
    '''
    if a.pontuacao > b.pontuacao or (a.pontuacao == b.pontuacao \
                                     and a.inscricao < b.inscricao):
        classificado = a
    else: #    a.pontuacao < b.pontuacao or (a.pontuacao == b.pontuacao and a.inscricao > b.inscricao):
        classificado = b
    return Posicao(p.x,p.y,p.z)
