from dataclasses import dataclass
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
    Receita = 250000.0, Lucro = 0
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
    return print('Receita = ', receita, ', Lucro = ', lucro, sep='')

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

class TipoProduto(Enum):
    ''' Representa os tipos de produtos que causam ruptura no estoque '''
    BOBINA = auto()
    CHAPA = auto()
    PAINEL = auto()
    NENHUM = auto()

assert len(relatorio) > 0
   
# Calcula o lucro de cada vendedor
cada_vendedor = []
for x in relatorio:
    if x.produto == TipoProduto.BOBINA:
        lucro_por_vendedor = lucro_por_vendedor + x.quantidade * (x.valor_com_desconto - CUSTO_BOBINA)
    elif x.produto == TipoProduto.CHAPA:
        lucro_por_vendedor = lucro_por_vendedor + x.quantidade * (x.valor_com_desconto - CUSTO_CHAPA)
    else: # x.produto == Tipo.Produto.PAINEL
        lucro_por_vendedor = lucro_por_vendedor + x.quantidade * (x.valor_com_desconto - CUSTO_PAINEL)
    cada_vendedor.append(Vendedor_Premiado(x.vendedor,lucro_por_vendedor))

# Identifica se existem vendedores repetidos. Se existe, soma o lucro deles.
indice_repetidos = []
for y in range(len(cada_vendedor)):
    for z in range(y + 1,len(cada_vendedor)):
        if cada_vendedor[y].nome == cada_vendedor[z].nome:
            y.lucro_por_vendedor = y.lucro_por_vendedor + z.lucro_por_vendedor
            indice_repetidos.append(z)
for i in range(len(indice_repetidos)):
    cada_vendedor = cada_vendedor[:indice_repetidos(i)] + cada_vendedor[indice_repetidos(i)+1:]
    for k in range(i+1,len(indice_repetidos)):
        indice_repetidos[k] = indice_repetidos[k] - 1













            # Definindo o segundo com maior lucro
    for s in range(len(cada_vendedor)) and s != v:
        for s1 in range(s + 1, len(cada_vendedor)):
            if cada_vendedor[s].lucro_por_vendedor > cada_vendedor[s1].lucro_por_vendedor:
                lista_premiados[1] = [Vendedor_Premiado(cada_vendedor[s].nome,cada_vendedor[s].lucro_por_vendedor)]
    
    # Definindo o terceiro com maior lucro
    for o in range(len(cada_vendedor)) and o != v and o != s:
        for o1 in range(o + 1, len(cada_vendedor)):
            if cada_vendedor[o].lucro_por_vendedor > cada_vendedor[o1].lucro_por_vendedor:
                lista_premiados[2] = [Vendedor_Premiado(cada_vendedor[o].nome,cada_vendedor[o].lucro_por_vendedor)]