# -*- coding: utf-8 -*-
"""
Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa.
O programa vai ler o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS 
ele irá pagar.

calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário 
ou então o empréstimo será negado.
"""


valor_casa = float(input('qual o valor da casa? '))

salario = float(input('qual o seu salario? '))

ano_pagamento = int(input('em quantos anos voce ira pagar? '))

parcela = valor_casa / ( ano_pagamento * 12 )


if parcela <= ( 0.3 * salario ):
    print('Emprestimo Aprovado')
    print('Sua parcela mensal será de {:.2f R$}'.format(parcela))
else:
    print('O seu emprestimo não foi aprovado, MULA!')