# -*- coding: utf-8 -*-
"""
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a
média de todos os valores e qual foi o maior e o menor valores lidos. o programa deve perguntar
ao usuário se ele quer ou não continuar a digitar valores
"""

n = 1
maior = 0
menor = 9999999
media = 0
quant = 0


while n != 0:
   n = int(input('Digite um valor[0 para sair]: '))
   if n < menor and  n != 0:
       menor = n
   elif n > maior :
       maior = n
            
   if n != 0:
      media += n
      quant += 1
    
media = media / quant
    
print('A média dos valores informado, em um total de {}, foi de {}'.format(quant, media))
print('O maior numero foi {} e o menor {}'.format(maior, menor))
    
    