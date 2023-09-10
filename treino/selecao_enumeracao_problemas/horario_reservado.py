from dataclasses import dataclass
# Analise
# Verifica se duas reservas em uma sala de reunião podem ser atendidas, não tendo conflitos de horarios. A sala de reunião possui horários
# disponiveis das 8:00h até as 18:00

# Tipos de dados
# Os horários das reuniões estarão dentro de uma estrutura.

@dataclass
class Horario:
    '''
    Representa um horário em minutos e segundos.
    '''
    hora: int
    minutos: int

@dataclass
class Reserva:
    '''
    Representa o horario de inicio e de fim de uma reunião
    '''
    horario_inicio: Horario
    horario_fim: Horario

def horario_reservado(a: Reserva, b: Reserva) -> bool:
    '''
    Verifica se as reservas *a* e *b* pode ser atendidas, sem conflitos de horários. Os horários disponiveis para reserva são das 8:00h 
    até as 18:00h.
    Exemplos
    >>> horario_reservado(Reserva(Horario(9,0),Horario(10,0)),Reserva(Horario(10,0),Horario(11,0)))
    True
    >>> horario_reservado(Reserva(Horario(9,0),Horario(10,0)),Reserva(Horario(9,30),Horario(11,0)))
    False
    '''
    if a.horario_inicio.hora == b.horario_inicio.hora and ((a.horario_inicio.hora > 8 and b.horario_inicio.hora > 8) and \
                                                           (a.horario_inicio.hora < 18 and b.horario_inicio.hora < 18)):
        if a.horario_inicio.minutos >= b.horario_fim.minutos or b.horario_inicio.minutos >= a.horario_fim.minutos:
            disponibilidade = True
        elif a.horario_inicio.minutos < b.horario_fim.minutos or b.horario_inicio.minutos < a.horario_fim.minutos:
            disponibilidade = False
        else: #a.horario_inicio.minutos == b.horario_inicio.minutos:
            disponibilidade = False
    elif a.horario_inicio.hora >= b.horario_fim.hora or b.horario_inicio.hora >= a.horario_fim.hora and ((a.horario_inicio.hora > 8 and \
                                                                                                          b.horario_inicio.hora > 8) and (a.horario_inicio.hora < 18 and b.horario_inicio.hora < 18)):
        disponibilidade = True
    else:
        disponibilidade= False
    return disponibilidade
    



