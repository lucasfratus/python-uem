from dataclasses import dataclass
# Analise
# Determina, entre dois times de futebol, qual possui o melhor desempenho. O desempenho é determinado na seguinte ordem:
# pelo número de pontos, número de vitórias e saldo de gols (diferenças entre todos os gols marcados e sofridos). Caso dois
# times empatem nesses critérios, a ordem alfabética dos nomes é usado para desempate. Caso os gols marcados forem menores que gols sofridos,
# o saldo não passa de 0, ou seja, não fica negativo.

# Tipos de dados
# O nome do time será uma string
# O número de pontos, número de vitórias e saldo de gols serão representados em uma estrutura.
# Pontos, vtórias e saldo de gols números inteiros positivos

@dataclass
class Time:
    nome: str
    pontos: int
    vitorias: int
    saldo: int

def melhor_desempenho(a: Time, b: Time) -> Time:
    '''
    Determina, entre os times *a* e *b*, qual possui o melhor desempenho. O desempenho é determinado na seguinte ordem:
    pelo número de pontos, número de vitórias e saldo de gols (diferenças entre todos os gols marcados e sofridos). Caso dois
    times empatem nesses critérios, a ordem alfabética dos nomes é usado para desempate. 
    O time *a* é aquele que, em ordem alfabética, sempre vem em primeiro, o time *b* é o outro.
    Caso os gols marcados forem menores que gols sofridos, o saldo não passa de 0, ou seja, não fica negativo.
    Exemplos
    >>> melhor_desempenho(Time('a',12,4,8),Time('b',10,4,8)).nome
    'a'
    >>> melhor_desempenho(Time('a',12,5,7),Time('b',12,4,8)).nome
    'a'
    >>> melhor_desempenho(Time('a',12,5,7),Time('b',12,5,8)).nome
    'b'
    >>> melhor_desempenho(Time('a',12,5,7),Time('b',12,5,7)).nome
    'a'
    '''
    if a.pontos > b.pontos:
        melhor = a
    elif a.vitorias > b.vitorias and a.pontos == b.pontos:
        melhor = a
    elif a.saldo > b.saldo and a.pontos == b.pontos and a.vitorias == b.vitorias:
        melhor = a
    else:
        melhor = b
    return melhor
