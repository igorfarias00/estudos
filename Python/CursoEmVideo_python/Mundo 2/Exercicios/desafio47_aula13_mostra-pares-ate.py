# -*- coding: utf-8 -*-
"""
'''faça um programa que mostre na tela todos os números pares que estão 
no intervalo entre 1 e 50'''

"""

for c in range(0,50, 2):  #percorre o intervalo de 0 a 50 pulando de dois em dois
    print(c, end=' ')
    

for c in range(1,50):   #percorre o intervalo de 1 a 50 e testa se o resto da divisao por 2 é 0
    if c % 2 == 0:
        print('\033[2;34;42m' , c, end=' ')
        
   