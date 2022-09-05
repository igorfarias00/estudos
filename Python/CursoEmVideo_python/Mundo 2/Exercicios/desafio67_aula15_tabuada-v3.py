# -*- coding: utf-8 -*-
"""
faça um programa que mostra a tabuada de vários números, um de cada vez, para cada valor
digitado pelo o usúario. O programa será interrompido quando o número solicitado for 
negativo.

"""

while True:
    n = int(input('Digite um número para saber a tabuada[número negativo para sair]: '))
    if n < 0:
        break
    
    print('-' * 30)
    cont = 1
    
    while cont <= 10:    
        print(f'{n} x  {cont} = {n * cont}')
        cont += 1
        
        
    print('-*' * 15)
        
print('TCHAU!')