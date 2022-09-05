# -*- coding: utf-8 -*-
"""
'''leia um numero e diga se ele é ou não primo'''
"""

n = int(input('\033[0;0;0mDigite um numero: '))

cont = 0


for c in range(1, n +1):
    if n % c == 0:
        print('\033[1;37;42m',  c, end=' ')
        cont += 1
        
    else:
        print('\033[1;34;41m', c, end=' ')
        
if cont == 2:
   print('\n\033[m O número é primo!  ')
else:
     print('\n\033[m O número não é primo! ')
        