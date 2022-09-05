# -*- coding: utf-8 -*-
"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista

No fina, mostre qual foi o maior e o menor valor digitado e as suas 
respectivas posições na lista

"""

num = []
pos_menor = []
pos_maior = []
c = maior = menor = 0

for c in range(0,5):
    num.append(int(input('Digite um número: ')))
    

        
for c in range(0,5):        #verifica qual é o maior e o menor no laço
    if c == 0:
        maior = num[c]
        menor = num[c]
    
    elif num[c] > maior:
        maior = num[c]
         
    if num[c] < menor:
        menor = num[c]

    
for c in range(0,5):        # verifica onde apareçe os maiores e menores
    if num[c] == menor:
        pos_menor.append(c)
    if num[c] == maior:
        pos_maior.append(c)
        
        
    
print(f'O maior valor foi {maior} na posição {pos_maior}')
print(f'O menor valor foi {menor} na posição {pos_menor}')