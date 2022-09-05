# -*- coding: utf-8 -*-
"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando
o seu PREÇO NORMAL e CONDIÇÃO de PAGAMENTO:
    
    -à vista dinheiro/cheque: 10% de desconto
    
    - Á vista no cartão: 5% de desconto
    
    -em até 2x no cartão: preço normal
    
    -em 3X ou mais no cartão: 2% de juros
"""

preco = float(input('Digite o Valor do Produto: '))

print('Qual a Forma de pagamento?')

pagamento = int(input('1 - á Vista dinheiro/cheque | 2 - á vista no cartão | 3 - parcelado no cartão | '))

if pagamento == 3:
    num_parcelas = int(input('Digite em quantas parcelas deseja pagar: '))
    if num_parcelas <=  2:
        print('Você ira pagar {:.2f} em {} parcelas de {:.2f} reais'.format(preco, num_parcelas, preco / num_parcelas))# preço normal
    else: 
        total = preco + preco * 0.2 
        print('Você ira pagar {:.2f} em {} parcelas de {:.2f} reais'.format(total, num_parcelas, total / num_parcelas))
        
elif pagamento == 2:
    total = preco - preco * 0.05
    print('Você Recebeu um desconto de 5%, ira pagar {:.2f} reais'.format(total))

elif pagamento == 1:
    total = preco - preco * 0.1
    print('Você Recebeu um desconto de 10%, ira pagar {:.2f} reais'.format(total))
else:
    print('WHHHHAAAAAT!')