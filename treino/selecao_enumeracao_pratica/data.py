from dataclasses import dataclass
# Analise
# Representa uma data com dia, mês e ano.

# Tipos de dados
# Dia, mês e ano serão uma estrutura.

@dataclass
class Data:
    '''
    Representa a data em dia, mês e ano.
    '''
    dia: int
    mes: int
    ano: int

def ultimo_dia(d: Data) -> bool:
    '''
    Produz True se a data inserida for o último dia daquele ano. Caso contrário, produz false
    Exemplos
    >>> ultimo_dia(Data(31,12,2023))
    True
    >>> ultimo_dia(Data('20','12','2023'))
    False
    '''
    return d.dia == 31 and d.mes == 12

def comparacao_data(d: Data, f: Data) -> bool:
    '''
    Produz True se *d* vem antes de *f*. Caso contrário, produz False. Se forem iguais, produz False. O mes e o dia não podem começar com "0"
    Exemplos
    >>> comparacao_data(Data(22, 1 , 2023), Data(23, 1, 2023))
    True
    >>> comparacao_data(Data(24, 1 , 2023), Data(23, 1, 2023))
    False
    >>> comparacao_data(Data(24, 1 , 2023), Data(24, 1, 2023))
    False
    '''
    if d.ano == f.ano:
        if d.mes == f.mes:
            if d.dia == f.dia:
                comparacao = False
            else: # d.dia != f.dia
                if d.dia < f.dia:
                    comparacao = True
                else: #d.dia > f.dia
                    comparacao = False
        else: # d.mes != f.mes
            if d.mes < f.mes:
                comparacao = True
            else: # d.mes > f.mes
                comparacao = False
    else: # d.ano != f.ano
        if d.ano < f.ano:
            comparacao = True
        else: # d.ano > f.ano
            comparacao = False
    return comparacao
            

    


        

    