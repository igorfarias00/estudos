# -*- coding: utf-8 -*-
"""

faça um programa que leia um número qualquer e mostre o seu fatorial

"""

n = int(input('Digite um número para saber seu fatorial: '))

fat = n          # fatorial reccebe o primeiro termo
c = n - 1        # prepara o segundo termo

while c != 0:       #enquanto o fatorial nao chegar a zero
    fat = fat * c   # fatorial * termo seguinte
    #print(fat)     # debug do fatorial
    c -= 1          # proximo termo
    
print('O fatorial de {} é {}'.format(n, fat))