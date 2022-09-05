# -*- coding: utf-8 -*-
"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
o valor 999, que é a condição de parada. No final mostre quantos números foram digitados e qual 
foi a sua soma entre eles
"""

n = 0
soma = 0
i = 0

while n != 999:
    n = int(input('Digite um numero para somar[digite 999 para parar]'))
    if n != 999:
        soma += n 
        i += 1
    
    
print('A soma total dos foi de {} e foram digitados {} números.'.format(soma, i))