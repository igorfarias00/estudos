# -*- coding: utf-8 -*-
"""
'''Refaça o desafio 9, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for'''

"""

num = int(input('Digite o número da tabuada: '))

for c in range(0, 11):
    print('{:2} * {} = {}'.format(c, num, num * c))