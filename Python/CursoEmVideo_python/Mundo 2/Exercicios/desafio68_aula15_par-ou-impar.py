# -*- coding: utf-8 -*-
"""
Faça um programa que jogue par ou ímpar com o computador. o jogo só será interrompido 
quando o jogador PERDER, mostrando o total de vezes vitórias consecutivas que ele 
conquistou no final do jogo.

"""

import random

par_impar = ''

vitoria = 0
while True:
    pc  = random.randint(1, 2)
   
    
  
    par_impar =  str(input('Par ou impar?')).lower()
    
    jogador = int(input('Digite um número: '))
    
    if par_impar == 'par' and (pc%2 == 1 and jogador % 2 == 0) or (pc%2 == 0 and jogador % 2 == 1): 
        # se o jogador pedir par e o computador colocar um numero impar e aquele um par ou vice versa
        break
    elif par_impar == 'impar' and (pc%2 == 0 and jogador % 2 == 0):
        # se o jogador pedir impar e o pc colocar par e o jogador tambem
        break
    
    print('Você ganhou essa! ')
    vitoria += 1
    print('-><-' * 10)
    
print(f'Você perdeu essa, mas ganhou {vitoria} seguidas')