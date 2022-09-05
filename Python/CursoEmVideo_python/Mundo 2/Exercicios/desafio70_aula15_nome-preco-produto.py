# -*- coding: utf-8 -*-
"""

Crie um programa que leia o nome e o preço de vários produtos. O programa deverá 
perguntar se o usuário vai continuar. No final, mostre.
    A) Qual é o total gasto na compra
    B) Quantos produtos custam mais de R$1000.
    C) Qual é o nome do produto mais barato

"""

barato = total = quant_prod1000 = preco = soma = i = 0
n = produto = prod_barato = ''

print('Carrinho de compras', '-0'* 20)
while True:
    if n == 'n':
        break
        
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    
    if i == 0:
        barato = preco
        
    if preco > 1000 :
        quant_prod1000 += 1
    if preco <= barato:
        barato = preco
        prod_barato = produto
    
    soma += preco
    i+= 1
    
    n = str(input('Deseja continuar[S/N]? ')).lower()
    
print(f'O total gasto na compra foi de R${soma:.2f}')
print(f'hà {quant_prod1000} produtos acima de R$1000.00 ')
print(f'O produto mais barato foi o {prod_barato} que custa R${barato:.2f}')