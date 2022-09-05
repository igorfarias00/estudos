# -*- coding: utf-8 -*-
"""'
''' desenvolva um programa que leia  seis números inteiros e mostre 
a soma apenas daqueles que forem pares. Se o valor for ímpar, desconsidere-o.'''
"""
soma = 0
cont = 0
for c in range(0, 6):
    num = int(input('Digite o {} numero: '. format(c + 1)))
    if num % 2 == 0:
        soma += num
        cont += 1
    else:
        print('número impar, desconsiderado')
        
print('voce informou {} números pares e a soma foi: {}'.format(cont, soma))