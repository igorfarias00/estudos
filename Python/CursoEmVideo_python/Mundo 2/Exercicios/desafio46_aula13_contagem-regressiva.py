# -*- coding: utf-8 -*-
"""
'''faça um programa que mostre na tela uma contagem regressiva para o 
estouro de fogos de artificio, indo de 10 até 0, com uma pausa de um segundo entre eles.'''


"""
import time

for c in range(10, -1, -1):
    print(c)
    time.sleep(1)
    
    
    
print('\033[4;33;44m KAAAABOOOOOM!')