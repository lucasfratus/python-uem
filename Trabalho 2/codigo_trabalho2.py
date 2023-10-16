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
    2.0
    >>> nota_cada_alternativa(18)
    3.0
    >>> nota_cada_alternativa(0)
    6.0
    >>> nota_cada_alternativa(1)
    6.0
    '''
    divisao = somatorio_alternativas(resposta)
    if len(divisao) == 0:
        valor_cada_alternativa = 6.0
    else:
        valor_cada_alternativa = 6.0 / len(divisao)
    return valor_cada_alternativa

def soma_nota(lst: list[float]) -> float:
    '''
    Soma as notas de *lst*. *lst* não pode ser uma lista vazia.
    Exemplos:
    >>> soma_nota([1.2, 1.2, 1.2, 1.2, 1.2])
    6.0
    >>> soma_nota([2.0, 0.0, 0.0, 0.0, 2.0])
    4.0
    >>> soma_nota([0.0, 0.0, 0.0, 0.0, 0.0])
    0.0
    '''
    nota_somada = 0.0
    for x in range(len(lst)):
        if x == 0:
            nota_somada = lst[x]
        else:
            nota_somada = lst[x] + soma_nota(lst[:x])
    return nota_somada


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
    >>> calcular_nota(Candidato(134698,115,[12,16,4,2,16]), [13,16,5,2,18]) 
    22.0
    >>> calcular_nota(Candidato(134698,115,[12,16,4,2,16]), [13,16,5,2,31]) 
    20.2
    '''  
    nota = 0.0
    for x in range(len(prova.respostas)):
        somatoria_respostas = somatorio_alternativas(prova.respostas[x])
        somatoria_gabarito = somatorio_alternativas(gabarito[x])
        nota_alt = [] # representa uma lista com os valores de cada alternativa
        nota_alt.append(nota_cada_alternativa(gabarito[x])) # adiciona o valor de cada alternativa em nota_alt
        if somatoria_respostas == [] and somatoria_gabarito == []:
            somatoria_respostas = [0]
            somatoria_gabarito = [0]
        for y in range(len(somatoria_respostas)):
            if somatoria_respostas[y] not in somatoria_gabarito:
                nota_alt = [0.0]
            elif somatoria_respostas[y] in somatoria_gabarito:
                nota = soma_nota(nota_alt) + nota
    return nota

def remover_redacao_zerada(lista_provas: list[Candidato]):
    '''
    Remove o candidato de *lista_provas* que foi desclassificado da prova, ou seja, tirou zero na redação
    '''
    i = 0
    while i < len(lista_provas):
        t = lista_provas[i]
        if lista_provas[i].nota_redacao == 0.0:
            lista_provas[i] = lista_provas[len(lista_provas) - 1]
            lista_provas[len(lista_provas) - 1] = t
        i = i + 1    

def ordenar_lista(lista_provas: list[NotaCandidato]):
    '''
    Ordena *lista_provas* em ordem decrescente de notas.
    Não pode ser uma lista vazia.
    Exemplos:
    >>> x = [NotaCandidato(codigo=134698, nota_final=145.0), NotaCandidato(codigo=256469, nota_final=143.0)]
    >>> ordenar_lista(x)
    >>> x
    [NotaCandidato(codigo=134698, nota_final=145.0), NotaCandidato(codigo=256469, nota_final=143.0)]
    '''
    assert len(lista_provas) > 0
    x = 0
    while x < len(lista_provas):
        k = lista_provas[x]
        melhor_nota = lista_provas[x].nota_final
        for y in range(x + 1, len(lista_provas)):
            if lista_provas[y].nota_final > melhor_nota:
                melhor_nota = lista_provas[y].nota_final
                lista_provas[x] = lista_provas[y]
                lista_provas[y] = k
        x = x + 1

def desempenho_vestibular(lista_provas: list[Candidato], gabarito: list[int]) -> list[NotaCandidato]:
    '''
    Devolve uma nova lista a partir de *lista_provas*, com a nota de cada candidato não desclassificado da redação já calculada,
    ordenada de forma decrescente levando em conta a nota final dos participantes.
    A nota de cada participante é calculada a partir da nota da redação e da lista de respostas marcadas por ele, que é comparada com
    o gabarito da prova.
    Para um candidato ter sua nota calculada, ele deve estar classificado na redação, ou seja, não tirou zero nela.
    Cada nota final deve estar acompanhada do código de identificação de cada participante.
    Caso haja um empate de notas, o que aparecer na lista por ultimo será o que estará na frente do outro candidato que empatou com ele.
    Exemplos:
    >>> desempenho_vestibular([Candidato(134698,115.0,[13,16,5,2,18])],[13,16,5,2,18])
    [NotaCandidato(codigo=134698, nota_final=145.0)]
    >>> desempenho_vestibular([Candidato(134698,115.0,[13,16,5,2,18]),Candidato(256469,119.0,[13,16,6,2,18])],[13,16,5,2,18])
    [NotaCandidato(codigo=134698, nota_final=145.0), NotaCandidato(codigo=256469, nota_final=143.0)]
    >>> desempenho_vestibular([Candidato(134698,115.0,[13,16,5,2,18]), Candidato(777777,120.0,[13,16,5,2,18])],[13,16,5,2,18])
    [NotaCandidato(codigo=777777, nota_final=150.0), NotaCandidato(codigo=134698, nota_final=145.0)]
    >>> desempenho_vestibular([Candidato(134698,114.0,[13,16,5,2,18]), Candidato(777777,120.0,[14,16,5,2,18]), Candidato(123456,120.0,[13,16,5,2,18])],[13,16,5,2,18])
    [NotaCandidato(codigo=123456, nota_final=150.0), NotaCandidato(codigo=777777, nota_final=144.0), NotaCandidato(codigo=134698, nota_final=144.0)]
    
    '''
    lista_resultados = []
    for x in lista_provas:
        nota_somada_candidato = calcular_nota(x,gabarito) + x.nota_redacao
        lista_resultados.append(NotaCandidato(x.codigo,nota_somada_candidato))   
        ordenar_lista(lista_resultados)
    return lista_resultados

