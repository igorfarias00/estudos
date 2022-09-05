# -*- coding: utf-8 -*-
"""
crie um programa que tenha uma tupla única com nomes de produtos e seus 
respectivos preços, na sequência.

No final, mostre uma listagem de preços, organizando os dados em forma tabular
"""

prod_preco = (
    'caneta', 2.50,
    'tinta', 12.50,
    'pão', 4.00,
    'picanha', 70.00,
    'arroz', 25.00,
    'feijão', 15.00,
    'grão de bico', 10.50,
    'PTS', 10.00,
    'Aveia', 11.00
    )

i = 0
s = 'LISTAGEM DE PREÇOS'


print('='* 30)
print('{0: ^30}'.format(s))
print('='* 30)



for i in range(0 , len(prod_preco) , 2):
    print('{0:.<20}R$ {1:>6.2f}'.format(prod_preco[i], prod_preco[i+1]))