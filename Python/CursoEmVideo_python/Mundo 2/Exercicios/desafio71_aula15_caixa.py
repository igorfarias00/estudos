# -*- coding: utf-8 -*-
"""
Crie um programa que simule o funcionamento de um caixa eletrônico. No ínicio, pergunta 
ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar 
quantas cédulas de cada valor serão entregues.

    obs.: considere que o caixa possui cedulas de 
    50.00 R$
    20.00 R$
    10.00 R$
     1.00 R$
    
"""

resto = notas50 = notas20 = notas10 =  0.0

print('=' * 30)
print('Banco do CEV')
print('=' * 30)

saque = int(input('Que valor você deseja sacar? '))


while True:
    notas50 = int( saque / 50.0 )
    resto = saque % 50.0
    
    if resto != 0:
        notas20 = int( resto / 20.0 )
        resto = resto % 20.0
    else:
        break;
        
    if resto != 0:
            notas10 = int (resto / 10.0 )
            resto = int( resto % 10.0 ) 
    else:
        break
    
    break

#print(notas50, notas20, notas10, resto) # debug para ver se os calculos ficaram corretos 

if notas50 > 0:
    print(f'Total de {notas50} cédulas de R$50')
if notas20 > 0:
    print(f'Total de {notas20} cédulas de R$20')
if notas10 > 0:
    print(f'Total de {notas10} cédulas de R$10')
if resto > 0:
    print(f'Total de {resto} cédulas de R$1')

print('='*30)

print('Volte sempre ao Banco CEV! Tenha um bom dia!')
        

            
        