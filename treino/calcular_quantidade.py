lucro = float(input("Lucro desejado: "))
tipo = input("Tipo de Produto: ")
preço = float(input("Preço: "))

'''
Preços

Bobina: 50 - 60
Chapa: 40 - 48
Painel: 75 - 90
'''

if tipo == 'bobina':
    custo = 50.0
elif tipo == 'chapa':
    custo = 40.0
else:
    custo = 75.0

print (lucro / (preço - custo))



premiados([Nota('Fabio',TipoProduto.BOBINA,3200,55.00),Nota('Jair',TipoProduto.CHAPA,1600,45.00)])