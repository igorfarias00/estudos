# -*- coding: utf-8 -*-
"""

crie um programa que leia vários números inteiros do teclado. O programa só vai parar 
quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos
números foram digitados e qual foi a soma entre eles.

"""

n = s = cont = 0

while True:
    n = int(input('Digite um número[999 para sair]: '))
    if n == 999:
        break
    cont += 1
    s += n
    
print(f'Você digitou {cont} números e a soma foi de {s}')

