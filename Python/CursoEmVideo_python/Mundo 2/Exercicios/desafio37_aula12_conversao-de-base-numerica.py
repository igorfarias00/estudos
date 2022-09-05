# -*- coding: utf-8 -*-
"""
Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher
qual será a BASE DE CONVERSãO:
    
    1 - para binario
    2 - para octal
    3 - para hexadecimal

"""

num = int(input('Digite qual o numero que será convertido?  '))
conver = 0

print('Qual a base de conversão?')

opcao = int(input('''
| 1 - Binario 
| 2 - Octal 
| 3 - Hexadecimal  ''')) 

if opcao == 1:
    conver = bin(num)
    print(' O numero digitado em Binario é: {}'.format(conver))

elif opcao == 2:
    conver = oct(num)
    print(' O numero digitado em Octal é:{}'.format(conver))
    
elif opcao == 3:
    conver = hex(num)
    print(' O numero digitado em Hexadecimal é: {}'.format(conver))
else:
    print('OPCAO INVALIDA MULA')