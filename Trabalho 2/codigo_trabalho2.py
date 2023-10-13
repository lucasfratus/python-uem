# Analise
# Calcula a lista de alternativas que somadas geram um certo somatório. Cada alternativa deve ser um dos
# seguintes valores: 01, 02, 04, 08, 16. O somatório deve ser um número entre 0 e 31

# Tipos de dados
# O somatório será um inteiro positivo entre 0 e 31.


def somatorio_alternativas(s: int) -> list[int]:
    '''
    Calcula a lista de alternativas que somadas gera o somátorio *s*.
    Cada alternativa pode ser um dos valores: 1, 2, 4, 8, 16.
    Requer que *s* esteja no entre 0 e 31.
    Exemplos
    >>> somatorio_alternativas(0)
    []
    >>> somatorio_alternativas(1)
    [1]
    >>> somatorio_alternativas(21)
    [1, 4, 16]
    >>> somatorio_alternativas(10)
    [2, 8]
    >>> somatorio_alternativas(31)
    [1, 2, 4, 8, 16]
    '''
    alternativas = []
    alternativa = 1
    while s > 0:
        # Verifica se a alternativa faz parte do somatório s
        if s % 2 == 1:
            alternativas.append(alternativa)
        # Divide todas as alternativas que compõe o somatório s por 2
        s = s // 2
        
        # Procura a próxima alternativa
        alternativa = alternativa * 2
    return alternativas

from dataclasses import dataclass
# Análise
# Indica o desempenho de cada candidato que não foi desclassificado na redação(tirou uma nota diferente de zero)
# de uma lista a partir do seu desempenho na prova, gerando uma nova lista com o código e nota final de cada candidato. 
# Cada prova possui um código de candidato,uma nota de redação(0 a 120) e uma lista com as respostas 
# das questões da prova. Caso o candidato marque uma alternativa que não está no gabarito, 
# a nota do participante naquela questão é zerada.
# Cada código de prova só aparece uma vez em cada lista, já que só existe a possibilidade de cada 
# candidato realizar uma única prova.
#
# Tipos de Dados
# A lista de provas será uma lista de estruturas.
# O gabarito será uma lista de inteiros.

@dataclass
class Candidato:
    '''
    Representa o candidato do vestibular, indicando seu código, nota da redação e uma lista de respostas da prova.
    '''
    codigo: int
    nota_redacao: int
    respostas: list[int]

@dataclass
class NotaCandidato:
    '''
    Representa a nota de cada candidato, indicando seu código e sua nota final.
    '''
    codigo: int
    nota_final: float


def nota_cada_alternativa(resposta:int) -> float:
    '''
    Calcula o valor de cada alternativa correta de uma questão.
    Cada questão vale 6.0, sendo dividida em possiveis 5 alternativas.
    Se a questão possui 5 corretas, cada alternativa correta vale 1.2.
    Se a questão possui 4 corretas, cada alternativa correta vale 1.5.
    Se a questão possui 3 corretas, cada alternativa correta vale 2.0.
    Se a questão possui 2 corretas, cada alternativa correta vale 3.0.
    Se a questão possui 1 correta, a alternativa correta vale 6.0
    Se a questão possui 0 corretas, a alternativa correta é 0, ou seja,vale 6.0
    Exemplos:
    >>> nota_cada_alternativa(31)
    1.2
    >>> nota_cada_alternativa(30)
    1.5
    >>> nota_cada_alternativa(28)
    2.0
    >>> nota_cada_alternativa(13)
    3.0
    >>> nota_cada_alternativa(0)
    6.0
    >>> nota_cada_alternativa(1)
    6.0
    '''
    divisao = somatorio_alternativas(resposta)
    if len(divisao) == 0 or len(divisao) == 1:
        valor_cada_alternativa = 6.0
    if len(divisao) == 2:
        valor_cada_alternativa = 3.0  
    if len(divisao) == 3:
        valor_cada_alternativa = 2.0  
    if len(divisao) == 4:
        valor_cada_alternativa = 1.5 
    if len(divisao) == 5: 
        valor_cada_alternativa = 1.2
    return valor_cada_alternativa


def calcular_nota(prova: Candidato, gabarito: list[int]) -> float:
    '''
    Calcula a nota de uma prova, levando em conta as respostas candidato e o gabarito da prova, não levando em conta a nota da redação.
    Exemplos
    >>> calcular_nota(Candidato(134698,115,[13,16,5,2,18]), [13,16,5,2,18])
    30.0
    >>> calcular_nota(Candidato(134698,115,[13,16,5,2,0]), [13,16,5,2,18])
    24.0
    >>> calcular_nota(Candidato(134698,115,[13,16,5,2,19]), [13,16,5,2,18])
    24.0
    >>> calcular_nota(Candidato(134698,115,[12,16,5,2,18]), [13,16,5,2,18])
    28.0
    >>> calcular_nota(Candidato(134698,115,[14,18,6,16,24]), [13,16,5,2,18])
    0.0
    >>> calcular_nota(Candidato(134698,115,[12,16,4,2,16], [13,16,5,2,18]) # 4.0 + 6.0 + 3.0 + 6.0 + 3.0
    22.0
    >>> calcular_nota(Candidato(134698,115,[12,16,4,2,16], [13,16,5,2,31]) # 4.0 + 6.0 + 3.0 + 6.0 + 1.2
    20.2
    '''  
    nota = 0
    for x in range(len(prova.respostas)):
        somatoria_respostas = somatorio_alternativas(prova.respostas[x])
        somatoria_gabarito = somatorio_alternativas(gabarito[x])
        nota_alt = nota_cada_alternativa(gabarito[x])
        if somatoria_respostas == [] and somatoria_gabarito == []:
            somatoria_respostas = [0]
            somatoria_gabarito = [0]
        for y in range(len(somatoria_respostas)):
            if somatoria_respostas[y] in somatoria_gabarito:
                nota = nota + nota_alt
            else:
                nota_alt = 0
    return nota

def desempenho_vestibular(lista_provas: list[Candidato], gabarito: list[int]) -> list[NotaCandidato]:
    '''
    Devolve uma nova lista a partir de *lista_provas*, com a nota de cada candidato não desclassificado da redação já calculada,
    ordenada de forma decrescente levando em conta a nota final dos participantes.
    A nota de cada participante é calculada a partir da nota da redação e da lista de respostas marcadas por ele, que é comparada com
    o gabarito da prova.
    Para um candidato ter sua nota calculada, ele deve estar classificado na redação, ou seja, não tirou zero nela.
    Cada nota final deve estar acompanhada do código de identificação de cada participante.
    Exemplos:
    >>> desempenho_vestibular([Candidato(134698,115.0,[13,16,5,2,18]),[13,16,5,2,18]])
    [NotaCandidato(134698,145.0)]
    >>> desempenho_vestibular([Candidato(134698,115.0,[13,16,5,2,18]),Candidato(256469,119.0,[13,16,6,2,18])],[13,16,5,2,18])
    [NotaCandidato(134698,145.0),NotaCandidato(256469,143.0)]
    '''
    lista_resultados = []
    for x in lista_provas:
        nota_somada_candidato = calcular_nota(x,gabarito) + x.nota_redacao
        lista_resultados.append(NotaCandidato(x.codigo,nota_somada_candidato))   
    return lista_resultados

