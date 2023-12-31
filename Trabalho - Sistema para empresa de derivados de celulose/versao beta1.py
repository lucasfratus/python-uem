from dataclasses import dataclass
from enum import Enum, auto
# Monitoramento de níveis de estoque
#
# Análise
# Totaliza a demanda de cada produto (podendo ser bobinas de papel, chapas de papelão e painéis de fibra de madeira) 
# a partir de uma lista de pedidos e verifica se algum produto causará uma ruptura, ou seja, se há uma demanda maior que o estoque.

# Tipos de dados
# A lista de pedidos será representada por uma estrutura. 

@dataclass
class Pedido:
    ''' Representa um pedido de um cliente.
    O número de cada produto deve ser positivo
    '''
    pedido_bobinas: int
    pedido_chapas: int
    pedido_paineis: int

@dataclass
class Totalizacao:
    ''' Representa a demanda total de cada produto
    O total de cada produto deve ser positivo
    '''
    total_bobinas: int
    total_chapas: int
    total_paineis: int

def totaliza_pedidos(pedidos: list[Pedido]) -> Totalizacao:
    '''
    Produz uma estrutura que totaliza a demanda de cada produto a partir de *pedidos*. 
    Os produtos são: bobinas de papel, chapas de papelão e painéis de fibra de madeira.
    A demanda de cada produto deve ser maior ou igual a zero.
    Se a lista de pedidos for vazia, a demanda total de todos os produtos será zero.
    
    Exemplos:
    >>> totaliza_pedidos([])
    Totalizacao(total_bobinas=0, total_chapas=0, total_paineis=0)
    >>> totaliza_pedidos([Pedido(4,3,2),Pedido(5,0,1),Pedido(2,7,4)])
    Totalizacao(total_bobinas=11, total_chapas=10, total_paineis=7)
    >>> totaliza_pedidos([Pedido(0,0,0),Pedido(0,0,0),Pedido(0,0,0)])
    Totalizacao(total_bobinas=0, total_chapas=0, total_paineis=0)
    >>> totaliza_pedidos([Pedido(1,3,2)])
    Totalizacao(total_bobinas=1, total_chapas=3, total_paineis=2)
    '''

    demanda = Totalizacao(0,0,0)
    for x in pedidos:
        demanda.total_bobinas = demanda.total_bobinas + x.pedido_bobinas
        demanda.total_chapas = demanda.total_chapas + x.pedido_chapas
        demanda.total_paineis = demanda.total_paineis + x.pedido_paineis
    return demanda

class TipoProduto(Enum):
    ''' Representa os tipos de produtos oferecidos pela empresa'''
    BOBINA = auto()
    CHAPA = auto()
    PAINEL = auto()
    NENHUM = auto() # Serve  para, quando for indicar uma ruptura de estoque

def ha_ruptura(estoque: Totalizacao, demanda: Totalizacao) -> list[TipoProduto]:
    '''
    Gera a partir de *estoque* e de *demanda* uma lista com os tipos de produtos com ruptura de estoque.
    Para acontecer uma ruptura, *demanda* deve ser maior que *estoque*.
    *estoque* e *demanda* devem maiores ou iguais a zero.
    
    Exemplos:
    >>> ha_ruptura(Totalizacao(6,4,2),Totalizacao(3,3,1))
    [<TipoProduto.NENHUM: 4>]
    >>> ha_ruptura(Totalizacao(3,2,1),Totalizacao(2,3,2))
    [<TipoProduto.CHAPA: 2>, <TipoProduto.PAINEL: 3>]
    >>> ha_ruptura(Totalizacao(2,2,1),Totalizacao(2,3,1))
    [<TipoProduto.CHAPA: 2>]
    >>> ha_ruptura(Totalizacao(2,2,2),Totalizacao(2,2,3))
    [<TipoProduto.PAINEL: 3>]
    >>> ha_ruptura(Totalizacao(6,4,3),Totalizacao(7,5,2))
    [<TipoProduto.BOBINA: 1>, <TipoProduto.CHAPA: 2>]
    >>> ha_ruptura(Totalizacao(6,5,2),Totalizacao(7,4,3))
    [<TipoProduto.BOBINA: 1>, <TipoProduto.PAINEL: 3>]
    >>> ha_ruptura(Totalizacao(6,5,2),Totalizacao(4,6,3))
    [<TipoProduto.CHAPA: 2>, <TipoProduto.PAINEL: 3>]
    >>> ha_ruptura(Totalizacao(6,4,3),Totalizacao(7,5,7))
    [<TipoProduto.BOBINA: 1>, <TipoProduto.CHAPA: 2>, <TipoProduto.PAINEL: 3>]
    '''
    produtos_ruptura = []

    if estoque.total_bobinas < demanda.total_bobinas:
        produtos_ruptura.append(TipoProduto.BOBINA)
    if estoque.total_chapas < demanda.total_chapas:
        produtos_ruptura.append(TipoProduto.CHAPA)
    if estoque.total_paineis < demanda.total_paineis:
        produtos_ruptura.append(TipoProduto.PAINEL)
    if estoque.total_bobinas >= demanda.total_bobinas and estoque.total_chapas >= demanda.total_chapas and estoque.total_paineis >= demanda.total_paineis:
        produtos_ruptura.append(TipoProduto.NENHUM)
    return produtos_ruptura

# Vendas
#
# Análise
# Determina a receita e o lucro líquido mensal a partir do relatório de vendas, onde cada nota de venda contém um campo indicando o nome do vendedor, o produto,
# a quantidade desse produto e o valor com desconto. Dependendo da quantidade de um produto, os vendedores podem oferecer um desconto aos clientes.
# O preço ofertado por cada vendedor não pode ser menor que o preço de custo do produto. Cada unidade de bobina de papel tem o preço de custo de 50,00 reais
# e o de venda de 60,00 reais. Cada chapa de papelão tem o preço de custo de 40,00 reais e o preço de venda de 48,00 reais. Já os painéis de fibra de
# madeira tem o custo de 75,00 e o preço de venda de 90,00. Além disso, após definir o lucro e a receita, 
# determina os três vendedores que mais geraram lucro no mês.
#
# Tipos de dados
# A lista será composta por notas de vendas.
# A nota de venda será representada por uma estrutura, composta pelo nome do vendedor(string), produto(tipo enumerado), 
# a quantidade desse produto(inteiro positivo) e o valor com desconto(float).



@dataclass
class Nota:
    ''' 
    Representa uma nota de vendas de uma empresa.
    É dividida em nome do vendedor, produto, quantidade do produto e o valor com desconto.
    O valor com desconto não pode ser menor que o preço de custo.
          
            Preço de custo de cada produto  X  Preço de venda
    Bobina:         50,00                         60,00
    
    Chapa:          40,00                         48,00

    Painel:         75,00                         90,00
    
    '''
    vendedor: str
    produto: TipoProduto
    quantidade: int
    valor_com_desconto: float

CUSTO_BOBINA = 50.00
CUSTO_CHAPA = 40.00
CUSTO_PAINEL = 75.00

def receita_lucro(relatorio: list[Nota]) -> float:
    '''
    Determina, a partir de *relatorio*, a receita e o lucro mensal de uma empresa. Cada nota de *relatorio* é composta pelo nome do vendedor,
    o produto, a quantidade do produto e o valor com desconto. 
    
    Exemplos:
    >>> receita_lucro([])
    Receita = 0, Lucro = 0
    >>> receita_lucro([Nota('Claudio',TipoProduto.BOBINA,5000,50.00)])
    Receita = 250000.0, Lucro = 0.0
    >>> receita_lucro([Nota('Lucas',TipoProduto.BOBINA,10000,53.00)])
    Receita = 530000.0, Lucro = 30000.0
    >>> receita_lucro([Nota('Pedro',TipoProduto.PAINEL,5000,85.00),Nota('Pedro',TipoProduto.CHAPA,4000,45.00)])
    Receita = 605000.0, Lucro = 70000.0
    >>> receita_lucro([Nota('Pedro',TipoProduto.BOBINA,1500,55.00),Nota('Daniela',TipoProduto.PAINEL,3000,80.00),Nota('Jonas',TipoProduto.CHAPA,1000,41.00)])
    Receita = 363500.0, Lucro = 23500.0
    >>> receita_lucro([Nota('Jaime',TipoProduto.PAINEL,2530,80.00),Nota('Daniel',TipoProduto.BOBINA,1000,52.00),Nota('Jaime',TipoProduto.PAINEL,2000,85.00)])
    Receita = 424400.0, Lucro = 34650.0
    '''
    receita = 0
    lucro = 0

    for x in relatorio:
        receita = receita + x.quantidade * x.valor_com_desconto
        if x.produto == TipoProduto.BOBINA:
            lucro = lucro + x.quantidade * (x.valor_com_desconto - CUSTO_BOBINA)
        elif x.produto == TipoProduto.CHAPA:
            lucro = lucro + x.quantidade * (x.valor_com_desconto - CUSTO_CHAPA)
        else: # x.produto == Tipo.Produto.PAINEL
            lucro = lucro + x.quantidade * (x.valor_com_desconto - CUSTO_PAINEL) 
    return receita, lucro

@dataclass
class Vendedor_Premiado:
    ''' 
    Representa cada vendedor premiado, indicando seu nome e lucro mensal
    '''
    nome: str
    lucro_por_vendedor: float
    soma_quantidades: int


def premiados(relatorio: list[Nota]) -> list[Vendedor_Premiado]:
    '''
    Determina, a partir de *relatorio*, os três vendedores que mais geraram lucro no mês, devolvendo uma nova lista. 
    Caso apareça mais de uma nota de umúnico vendedor em *relatorio*, 
    o lucro dessas notas é somado e levado em consideração quando os três vendedores forem determinados.
    *relatorio* não pode ser uma lista vazia.
    
    Exemplos:
    >>> premiados([Nota('Lucas',TipoProduto.BOBINA,20000,55.00)])
    [Vendedor_Premiado(nome='Lucas', soma_quantidades=20000, lucro_por_vendedor=100000.0), Vendedor_Premiado(nome='', soma_quantidades=0, lucro_por_vendedor=0.0), Vendedor_Premiado(nome='', soma_quantidades=0, lucro_por_vendedor=0.0)]
    >>> premiados([Nota('Fabio',TipoProduto.PAINEL,16000,80.00),Nota('Jair',TipoProduto.CHAPA,12000,45.00)])
<<<<<<< Updated upstream
    [Vendedor_Premiado(nome='Fabio', lucro_por_vendedor=80000.0), Vendedor_Premiado(nome='Jair', lucro_por_vendedor=60000.0), Vendedor_Premiado(nome='', lucro_por_vendedor=0.0)]
    
=======
    [Vendedor_Premiado(nome='Fabio', soma_quantidades=16000, lucro_por_vendedor=80000.0), Vendedor_Premiado(nome='Jair', soma_quantidades=0, lucro_por_vendedor=60000.0), Vendedor_Premiado(nome='', soma_quantidades=0, lucro_por_vendedor=0.0)]
>>>>>>> Stashed changes
    >>> premiados([Nota('Marcia',TipoProduto.CHAPA,24000,45.00),Nota('Paulo',TipoProduto.BOBINA,34000,55.00),Nota('Marcia',TipoProduto.PAINEL,16000,80.00)])        
    [Vendedor_Premiado(nome='Marcia', soma_quantidades=0, lucro_por_vendedor=200000.0), Vendedor_Premiado(nome='Paulo', soma_quantidades=0, lucro_por_vendedor=170000.0), Vendedor_Premiado(nome='', soma_quantidades=0, lucro_por_vendedor=0.0)]
    >>> premiados([Nota('Marcia',TipoProduto.CHAPA,24000,45.00),Nota('Paulo',TipoProduto.BOBINA,34000,55.00),Nota('Marcia',TipoProduto.PAINEL,16000,80.00),Nota('Paulo',TipoProduto.CHAPA,8000,45.00)])
    [Vendedor_Premiado(nome='Paulo', soma_quantidades=0, lucro_por_vendedor=210000.0), Vendedor_Premiado(nome='Marcia', soma_quantidades=0, lucro_por_vendedor=200000.0), Vendedor_Premiado(nome='', soma_quantidades=0, lucro_por_vendedor=0.0)]
    >>> premiados([Nota('Carlos',TipoProduto.BOBINA,30000,55.00),Nota('Luan',TipoProduto.CHAPA,28000,45.00), Nota('Lucia',TipoProduto.PAINEL,32000,80.00), Nota('Fabricio',TipoProduto.CHAPA,29000,45.00)]) 
<<<<<<< Updated upstream
    [Vendedor_Premiado(nome='Lucia', lucro_por_vendedor=160000.0), Vendedor_Premiado(nome='Carlos', lucro_por_vendedor=150000.0), Vendedor_Premiado(nome='Fabricio', lucro_por_vendedor=145000.0)]
    >>> premiados([Nota('Carlos',TipoProduto.BOBINA,30000,55.00),Nota('Luan',TipoProduto.CHAPA,28000,45.00), Nota('Lucia',TipoProduto.PAINEL,32000,80.00), Nota('Fabricio',TipoProduto.CHAPA,29000,45.00), Nota('Paulo',TipoProduto.PAINEL,16000,55.00)])
    [Vendedor_Premiado(nome='pAU', lucro_por_vendedor=160000.0), Vendedor_Premiado(nome='Carlos', lucro_por_vendedor=150000.0), Vendedor_Premiado(nome='Fabricio', lucro_por_vendedor=145000.0)]
=======
    [Vendedor_Premiado(nome='Lucia', soma_quantidades=0, lucro_por_vendedor=160000.0), Vendedor_Premiado(nome='Carlos', soma_quantidades=0, lucro_por_vendedor=150000.0), Vendedor_Premiado(nome='Fabricio', soma_quantidades=0, lucro_por_vendedor=145000.0)]
    >>> premiados([Nota('Carlos',TipoProduto.BOBINA,30000,55.00),Nota('Luan',TipoProduto.CHAPA,28000,45.00), Nota('Lucia',TipoProduto.PAINEL,32000,80.00), Nota('Fabricio',TipoProduto.CHAPA,29000,45.00), Nota('Paulo',TipoProduto.BOBINA,28000,55.00)])
    [Vendedor_Premiado(nome='Lucia', soma_quantidades=0, lucro_por_vendedor=160000.0), Vendedor_Premiado(nome='Carlos', soma_quantidades=0, lucro_por_vendedor=150000.0), Vendedor_Premiado(nome='Fabricio', soma_quantidades=0, lucro_por_vendedor=145000.0)]
>>>>>>> Stashed changes
    '''

    assert len(relatorio) > 0
   
    # Calcula o lucro de cada vendedor
    cada_vendedor = []
    for x in relatorio:
        lucro_por_vendedor = 0.0
        soma_quantidades = 0.0
        if x.produto == TipoProduto.BOBINA:
            lucro_por_vendedor = lucro_por_vendedor + x.quantidade * (x.valor_com_desconto - CUSTO_BOBINA)
        elif x.produto == TipoProduto.CHAPA:
            lucro_por_vendedor = lucro_por_vendedor + x.quantidade * (x.valor_com_desconto - CUSTO_CHAPA)
        else: # x.produto == Tipo.Produto.PAINEL
            lucro_por_vendedor = lucro_por_vendedor + x.quantidade * (x.valor_com_desconto - CUSTO_PAINEL)
        soma_quantidades = soma_quantidades + x.quantidade
        cada_vendedor.append(Vendedor_Premiado(x.vendedor, soma_quantidades, lucro_por_vendedor))

    # Identifica se existem vendedores repetidos. Se existe, soma o lucro deles.
    indice_repetidos_desordenados = []
    for y in range(len(cada_vendedor)):
        for z in range(y + 1, len(cada_vendedor)):
            if cada_vendedor[y].nome == cada_vendedor[z].nome:
                cada_vendedor[y].lucro_por_vendedor = cada_vendedor[y].lucro_por_vendedor + cada_vendedor[z].lucro_por_vendedor
<<<<<<< Updated upstream
                incluso = False
                for indice in indice_repetidos_desordenados:
                    if z == indice:
                        incluso = True
                if incluso == False:
                    indice_repetidos_desordenados.append(z)
    
    indice_repetidos_ordenados = []
    while indice_repetidos_desordenados:
        menor_valor = indice_repetidos_desordenados[0]
        for x in indice_repetidos_desordenados:
            if x < menor_valor:
                menor_valor = x
            for y in range(indice_repetidos_desordenados):
                indice_repetidos_desordenados[:y] + indice_repetidos_desordenados[y+1:]
            indice_repetidos_ordenados.append(menor_valor)

<<<<<<< HEAD:Trabalho - Sistema para empresa de derivados de celulose/sistema_empresa_derivados_de_celulose.py
=======
    #for i in range(len(indice_repetidos)):
        #cada_vendedor = cada_vendedor[:indice_repetidos[i]] + cada_vendedor[indice_repetidos[i] + 1:]
        #for k in range(i+1,len(indice_repetidos)):
            #indice_repetidos[k] = indice_repetidos[k] - 1
=======
                indice_repetidos.append(z)
    
    for i in range(len(indice_repetidos)):
        cada_vendedor = cada_vendedor[:indice_repetidos[i]] + cada_vendedor[indice_repetidos[i] + 1:]
        for k in range(i+1,len(indice_repetidos)):
            indice_repetidos[k] = indice_repetidos[k] - 1
>>>>>>> Stashed changes
>>>>>>> 05dc296e44f7a41f1c95669c3c799c9ab4a9628d:Trabalho - Sistema para empresa de derivados de celulose/versao beta.py

    # Define o ranking dos três vendedores que mais geraram lucro
    posicao1 = Vendedor_Premiado('',0.0)
    posicao2 = Vendedor_Premiado('',0.0)
    posicao3 = Vendedor_Premiado('',0.0)

    # Define o ranking dos vendedores
    for x in range(len(cada_vendedor)):
        for y in range(x + 1,)




    # Define o vendedor da primeira posição
    for vnd in range(len(cada_vendedor)):
        if cada_vendedor[vnd].lucro_por_vendedor > posicao1.lucro_por_vendedor:
            posicao1 = cada_vendedor[vnd]

    # Define o vendedor da segunda posição
    for vnd1 in range(len(cada_vendedor)): 
        if cada_vendedor[vnd1].lucro_por_vendedor > posicao2.lucro_por_vendedor and \
            cada_vendedor[vnd1].lucro_por_vendedor < posicao1.lucro_por_vendedor:
            posicao2 = cada_vendedor[vnd1]
    
    # Define o vendedor da terceira posição
    for vnd2 in range(len(cada_vendedor)):
        if cada_vendedor[vnd2].lucro_por_vendedor > posicao3.lucro_por_vendedor and \
            cada_vendedor[vnd2].lucro_por_vendedor < posicao2.lucro_por_vendedor:
            posicao3 = cada_vendedor[vnd2] 
    
    lista_premiados = [posicao1, posicao2, posicao3]
            
    return lista_premiados



