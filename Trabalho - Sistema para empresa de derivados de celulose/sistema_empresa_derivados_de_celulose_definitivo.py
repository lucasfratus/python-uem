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
    (0, 0)
    >>> receita_lucro([Nota('Claudio',TipoProduto.BOBINA,5000,50.00)])
    (250000.0, 0.0)
    >>> receita_lucro([Nota('Lucas',TipoProduto.BOBINA,10000,53.00)])
    (530000.0, 30000.0)
    >>> receita_lucro([Nota('Pedro',TipoProduto.PAINEL,5000,85.00),Nota('Pedro',TipoProduto.CHAPA,4000,45.00)])
    (605000.0, 70000.0)
    >>> receita_lucro([Nota('Pedro',TipoProduto.BOBINA,1500,55.00),Nota('Daniela',TipoProduto.PAINEL,3000,80.00),Nota('Jonas',TipoProduto.CHAPA,1000,41.00)])
    (363500.0, 23500.0)
    >>> receita_lucro([Nota('Jaime',TipoProduto.PAINEL,2530,80.00),Nota('Daniel',TipoProduto.BOBINA,1000,52.00),Nota('Jaime',TipoProduto.PAINEL,2000,85.00)])
    (424400.0, 34650.0)
    '''
    receita = 0
    lucro_total = 0

    for x in relatorio:
        receita = receita + x.quantidade * x.valor_com_desconto
        if x.produto == TipoProduto.BOBINA:
            lucro_total = lucro_total + x.quantidade * (x.valor_com_desconto - CUSTO_BOBINA)
        elif x.produto == TipoProduto.CHAPA:
            lucro_total =  lucro_total + x.quantidade * (x.valor_com_desconto - CUSTO_CHAPA)
        else: # x.produto == Tipo.Produto.PAINEL
            lucro_total = lucro_total + x.quantidade * (x.valor_com_desconto - CUSTO_PAINEL) 
    return receita,lucro_total

@dataclass
class Vendedor_Candidato:
    ''' 
    Representa cada vendedor candidato ao prêmio, indicando seu nome, quantidade de produtos vendida e lucro mensal.
    '''
    nome: str
    soma_quantidades: int
    lucro_por_vendedor: float

def lucro_vendedor(nota_vendedor: Nota) -> Vendedor_Candidato:
    '''
    Calcula o lucro de um vendedor a partir de *nota_vendedor*, que contém seu nome, o produto vendido, a quantidade e o valor com desconto.
    Exemplos:
    >>> lucro_vendedor(Nota('Pedro',TipoProduto.BOBINA,3200,55.00))
    Vendedor_Candidato(nome='Pedro', soma_quantidades=3200, lucro_por_vendedor=16000.0)
    >>> lucro_vendedor(Nota('Gabriel',TipoProduto.BOBINA,0,0.0))
    Vendedor_Candidato(nome='Gabriel', soma_quantidades=0, lucro_por_vendedor=0.0)
    >>> lucro_vendedor(Nota('',TipoProduto.BOBINA,0,0.0))
    Vendedor_Candidato(nome='', soma_quantidades=0, lucro_por_vendedor=0.0)
    '''
    lucro_por_vendedor = 0.0
    if nota_vendedor.produto == TipoProduto.BOBINA:
        lucro_por_vendedor = nota_vendedor.quantidade * (nota_vendedor.valor_com_desconto - CUSTO_BOBINA)
    elif nota_vendedor.produto == TipoProduto.CHAPA:
        lucro_por_vendedor = nota_vendedor.quantidade * (nota_vendedor.valor_com_desconto - CUSTO_CHAPA)
    else: # lucro_por_vendedor.produto == Tipo.Produto.PAINEL
        lucro_por_vendedor = nota_vendedor.quantidade * (nota_vendedor.valor_com_desconto - CUSTO_PAINEL)
    return Vendedor_Candidato(nota_vendedor.vendedor,nota_vendedor.quantidade,lucro_por_vendedor)

def repeticao_vendedor(lst: list[Vendedor_Candidato]) -> list[Vendedor_Candidato]:
    '''
    Verifica se um vendedor de *lst* aparece mais de uma vez. Caso apareça, soma os lucros das outras ocorrências na primeira ocorrência.
    Exemplos
    >>> repeticao_vendedor([Vendedor_Candidato('Lucas',20000,100000.0)])
    [Vendedor_Candidato(nome='Lucas', soma_quantidades=20000, lucro_por_vendedor=100000.0)]
    >>> repeticao_vendedor([Vendedor_Candidato('Lucas',20000,100000.0),Vendedor_Candidato('Lucas',2000,10000.0)])
    [Vendedor_Candidato(nome='Lucas', soma_quantidades=22000, lucro_por_vendedor=110000.0), Vendedor_Candidato(nome='Lucas', soma_quantidades=0.0, lucro_por_vendedor=0.0)]
    >>> repeticao_vendedor([Vendedor_Candidato('Lucas',20000,100000.0),Vendedor_Candidato('Fabio',20000,100000.0)])
    [Vendedor_Candidato(nome='Lucas', soma_quantidades=20000, lucro_por_vendedor=100000.0), Vendedor_Candidato(nome='Fabio', soma_quantidades=20000, lucro_por_vendedor=100000.0)]
    '''
    #for x in lst:
        #lucro_vendedor(x)
        #cada_vendedor.append(lucro_vendedor(x))
    
    if len(lst) > 1:
        for cv in range(len(lst)):
            for v in range(cv + 1, len(lst)):
                if lst[cv].nome == lst[v].nome:
                    lst[cv].lucro_por_vendedor = lst[cv].lucro_por_vendedor + \
                    lst[v].lucro_por_vendedor
                    lst[cv].soma_quantidades = lst[cv].soma_quantidades + \
                    lst[v].soma_quantidades
                    lst[v].lucro_por_vendedor = 0.0  # Zera o lucro das próximas vezes que o mesmo vendedor aparece.
                    lst[v].soma_quantidades = 0.0  # Zera a quantidade das próximas vezes que o mesmo vendedor aparece
    return lst

def maior(lst1: list[Vendedor_Candidato]) -> Vendedor_Candidato:
    '''
    Encontra o vendedor de *lst* com o maior lucro.
    Exemplos:
    >>> maior([])
    Vendedor_Candidato(nome='', soma_quantidades=0, lucro_por_vendedor=0.0)
    >>> maior([Vendedor_Candidato('Lucas',20000,100000.0)])
    Vendedor_Candidato(nome='Lucas', soma_quantidades=20000, lucro_por_vendedor=100000.0)
    >>> maior([Vendedor_Candidato('Carlos',30000,150000.0), Vendedor_Candidato('Luan',28000,140000.0), Vendedor_Candidato('Lucia',32000,160000.0), Vendedor_Candidato('Fabricio',29000,145000.0)]) 
    Vendedor_Candidato(nome='Lucia', soma_quantidades=32000, lucro_por_vendedor=160000.0)
    '''
    #for x in lst1:
        #lucro_vendedor(x)
        #lst.append(lucro_vendedor(x))

    maior_de_todos = Vendedor_Candidato('',0,0.0)
    for x in range(len(lst1)):
        if lst1[x].lucro_por_vendedor > maior_de_todos.lucro_por_vendedor and \
            lst1[x].lucro_por_vendedor > 0.0:
            maior_de_todos = lst1[x]
    
    return maior_de_todos

def indice_maior(lst2: list[Vendedor_Candidato]) -> int:
    '''
    Encontra o indice do vendedor de maior lucro de *lst*
    Exemplos:
    >>> indice_maior([Vendedor_Candidato('Lucas',20000,100000.0)])
    0
    >>> indice_maior([Vendedor_Candidato('Carlos',30000,150000.0), Vendedor_Candidato('Luan',28000,140000.0), Vendedor_Candidato('Lucia',32000,160000.0), Vendedor_Candidato('Fabricio',29000,145000.0)]) 
    2
    >>> indice_maior([Vendedor_Candidato('Lucas',20000,100000.0),Vendedor_Candidato('Lucas', 20000, 100000.0)])
    0
    '''
    i_maior_de_todos = 0
    if len(lst2) > 1:
        for x in range(len(lst2)):
            if lst2[x].lucro_por_vendedor > lst2[i_maior_de_todos].lucro_por_vendedor:
                i_maior_de_todos = x
    else:
        i_maior_de_todos

    return i_maior_de_todos
 
def premiados(relatorio: list[Nota]) -> list[Vendedor_Candidato]:
    '''
    Determina, a partir de *relatorio*, os três vendedores que mais geraram lucro no mês, devolvendo uma nova lista. 
    Caso apareça mais de uma nota de um único vendedor em *relatorio*, 
    o lucro dessas notas é somado e levado em consideração quando os três vendedores forem determinados.
    *relatorio* não pode ser uma lista vazia.
    Caso haja um empate entre os lucros de vendedores, a ordem deles no ranking será igual a ordem deles em *relatorio*.
    
    Exemplos:
    >>> premiados([])
    [Vendedor_Candidato(nome='', soma_quantidades=0, lucro_por_vendedor=0.0), Vendedor_Candidato(nome='', soma_quantidades=0, lucro_por_vendedor=0.0), Vendedor_Candidato(nome='', soma_quantidades=0, lucro_por_vendedor=0.0)]
    >>> premiados([Nota('Lucas',TipoProduto.BOBINA,20000,55.00)])
    [Vendedor_Candidato(nome='Lucas', soma_quantidades=20000, lucro_por_vendedor=100000.0), Vendedor_Candidato(nome='', soma_quantidades=0, lucro_por_vendedor=0.0), Vendedor_Candidato(nome='', soma_quantidades=0, lucro_por_vendedor=0.0)]
    >>> premiados([Nota('Fabio',TipoProduto.PAINEL,16000,80.00),Nota('Jair',TipoProduto.CHAPA,12000,45.00)])
    [Vendedor_Candidato(nome='Fabio', soma_quantidades=16000, lucro_por_vendedor=80000.0), Vendedor_Candidato(nome='Jair', soma_quantidades=12000, lucro_por_vendedor=60000.0), Vendedor_Candidato(nome='', soma_quantidades=0, lucro_por_vendedor=0.0)]
    >>> premiados([Nota('Pedro',TipoProduto.BOBINA,40000,55.00),Nota('Pedro',TipoProduto.PAINEL,20000,85.00)])
    [Vendedor_Candidato(nome='Pedro', soma_quantidades=60000, lucro_por_vendedor=400000.0), Vendedor_Candidato(nome='', soma_quantidades=0, lucro_por_vendedor=0.0), Vendedor_Candidato(nome='', soma_quantidades=0, lucro_por_vendedor=0.0)]
    >>> premiados([Nota('Marcia',TipoProduto.CHAPA,24000,45.00),Nota('Paulo',TipoProduto.BOBINA,34000,55.00),Nota('Marcia',TipoProduto.PAINEL,16000,80.00)])        
    [Vendedor_Candidato(nome='Marcia', soma_quantidades=40000, lucro_por_vendedor=200000.0), Vendedor_Candidato(nome='Paulo', soma_quantidades=34000, lucro_por_vendedor=170000.0), Vendedor_Candidato(nome='', soma_quantidades=0, lucro_por_vendedor=0.0)]
    >>> premiados([Nota('Marcia',TipoProduto.CHAPA,24000,45.00),Nota('Paulo',TipoProduto.BOBINA,34000,55.00),Nota('Marcia',TipoProduto.PAINEL,16000,80.00),Nota('Paulo',TipoProduto.CHAPA,8000,45.00),Nota('Marcia',TipoProduto.PAINEL,16000,80.00)])
    [Vendedor_Candidato(nome='Marcia', soma_quantidades=56000, lucro_por_vendedor=280000.0), Vendedor_Candidato(nome='Paulo', soma_quantidades=42000, lucro_por_vendedor=210000.0), Vendedor_Candidato(nome='', soma_quantidades=0, lucro_por_vendedor=0.0)]
    >>> premiados([Nota('Marcia',TipoProduto.CHAPA,24000,45.00),Nota('Paulo',TipoProduto.BOBINA,34000,55.00),Nota('Marcia',TipoProduto.PAINEL,16000,80.00),Nota('Paulo',TipoProduto.CHAPA,8000,45.00)])
    [Vendedor_Candidato(nome='Paulo', soma_quantidades=42000, lucro_por_vendedor=210000.0), Vendedor_Candidato(nome='Marcia', soma_quantidades=40000, lucro_por_vendedor=200000.0), Vendedor_Candidato(nome='', soma_quantidades=0, lucro_por_vendedor=0.0)]
    >>> premiados([Nota('Carlos',TipoProduto.BOBINA,30000,55.00),Nota('Luan',TipoProduto.CHAPA,28000,45.00), Nota('Lucia',TipoProduto.PAINEL,32000,80.00), Nota('Fabricio',TipoProduto.CHAPA,29000,45.00)]) 
    [Vendedor_Candidato(nome='Lucia', soma_quantidades=32000, lucro_por_vendedor=160000.0), Vendedor_Candidato(nome='Carlos', soma_quantidades=30000, lucro_por_vendedor=150000.0), Vendedor_Candidato(nome='Fabricio', soma_quantidades=29000, lucro_por_vendedor=145000.0)]
    >>> premiados([Nota('Carlos',TipoProduto.BOBINA,30000,55.00),Nota('Luan',TipoProduto.CHAPA,28000,45.00), Nota('Lucia',TipoProduto.PAINEL,32000,80.00), Nota('Fabricio',TipoProduto.CHAPA,29000,45.00), Nota('Paulo',TipoProduto.BOBINA,28000,55.00)])
    [Vendedor_Candidato(nome='Lucia', soma_quantidades=32000, lucro_por_vendedor=160000.0), Vendedor_Candidato(nome='Carlos', soma_quantidades=30000, lucro_por_vendedor=150000.0), Vendedor_Candidato(nome='Fabricio', soma_quantidades=29000, lucro_por_vendedor=145000.0)]
    >>> premiados([Nota('Carlos',TipoProduto.BOBINA,30000,55.00),Nota('Luan',TipoProduto.CHAPA,28000,45.00), Nota('Lucia',TipoProduto.PAINEL,32000,80.00), Nota('Fabricio',TipoProduto.CHAPA,29000,45.00), Nota('Paulo',TipoProduto.BOBINA,28000,55.00),Nota('Paulo',TipoProduto.BOBINA,28000,55.00)])
    [Vendedor_Candidato(nome='Paulo', soma_quantidades=56000, lucro_por_vendedor=280000.0), Vendedor_Candidato(nome='Lucia', soma_quantidades=32000, lucro_por_vendedor=160000.0), Vendedor_Candidato(nome='Carlos', soma_quantidades=30000, lucro_por_vendedor=150000.0)]
    >>> premiados([Nota('Carlos',TipoProduto.BOBINA,28000,55.00),Nota('Luan',TipoProduto.BOBINA,28000,55.00), Nota('Lucia',TipoProduto.BOBINA,28000,55.00), Nota('Fabricio',TipoProduto.BOBINA,28000,55.00), Nota('Paulo',TipoProduto.BOBINA,28000,55.00),Nota('Cesar',TipoProduto.BOBINA,28000,55.00)])
    [Vendedor_Candidato(nome='Carlos', soma_quantidades=28000, lucro_por_vendedor=140000.0), Vendedor_Candidato(nome='Luan', soma_quantidades=28000, lucro_por_vendedor=140000.0), Vendedor_Candidato(nome='Lucia', soma_quantidades=28000, lucro_por_vendedor=140000.0)]
    '''
    relatorio_definitivo = []
    
    for x in relatorio:
        lucro_vendedor(x)
        relatorio_definitivo.append(lucro_vendedor(x))
    cada_vendedor = repeticao_vendedor(relatorio_definitivo)

    ranking = []

    # Definindo o primeiro do rank:
    posicao1= maior(cada_vendedor)
    indice_p1 = indice_maior(cada_vendedor)
    cada_vendedor = cada_vendedor[:indice_p1] + cada_vendedor[indice_p1+1:]
    ranking.append(posicao1)

    # Definindo o segundo do rank
    posicao2= maior(cada_vendedor)
    indice_p2 = indice_maior(cada_vendedor)
    cada_vendedor = cada_vendedor[:indice_p2] + cada_vendedor[indice_p2+1:]
    ranking.append(posicao2)

    # Definindo o terceiro do rank
    posicao3= maior(cada_vendedor)
    ranking.append(posicao3)

    return ranking



