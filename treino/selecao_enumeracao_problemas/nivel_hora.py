# Análise
# Calcular o novo nivel do jogador com base no nivel atual e horas jogadas na semana.
# Os níveis no jogo são de 0 a 25
# Se durante a semana os jogadores jogarem:
# 4 a 5 horas permanecem no mesmo nivel.
# menos que 4 horas diminuem um nivel a cada hora que falta para chegar em 4.
# mais de 5 horas sobem um nível por hora, mas com limite de 7 níveis.

# Tipo de dados
# o nível será um inteiro positivo.
# As horas jogadas serão inteiros positivos.

def nivel_por_hora(nivel_atual: int, horas: int) -> int:
    '''
    Calcula o novo nível de um jogador com base em *horas* jogadas na semana e no *nivel_atual*.
    Os níveis no jogo vão de 0 a 25.
    Se *horas* >= 4 <= 5, o jogador permanece em *nivel_atual*.
    Se *horas* < 4, o jogador perde um nível a cada hora que falta para chegar em 4.
    Se *horas* > 5, o jogador sobe um nivel por hora, mas se limitando a 7 níveis subidos por semana.
    '''
    assert nivel_atual <= 25
    if horas >= 4 and horas <= 5:
        novo_nivel = nivel_atual
    elif horas > 5:
        novo_nivel = nivel_atual + 1 * (horas - 5)
    else: # horas < 4
        novo_nivel - 1 * (4 - horas)
    if novo_nivel - nivel_atual > 7:
        novo_nivel = nivel_atual + 7
    else: # novo_nivel - nivel_atual < 7
        novo_nivel
    return novo_nivel

