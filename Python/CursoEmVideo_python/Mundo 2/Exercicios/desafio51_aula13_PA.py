# -*- coding: utf-8 -*-
"""
''' desenvolva um programa que leia o primeiro termo e a razão de  um progressão aritimetica.
No final,mostre os  10 primeiros termos dessa progressão'''
"""

termo = int(input('Digite o primeiro termo da Progressão aritimética: '))
razao = int(input('Digite a razão da progressão: '))

decimo = termo + (10 - 1) * razao
 
for c in range(termo, decimo + razao, razao):
    print(c, end=' -> ')
    
"""  
for c in range(0, 10):
    print(termo)
    termo += razao
"""