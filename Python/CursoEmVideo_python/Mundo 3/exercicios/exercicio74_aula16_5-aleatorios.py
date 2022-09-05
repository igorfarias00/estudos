# -*- coding: utf-8 -*-
"""
crie um programa que ira gerar 5 números aleatórios e colocar em uma tupla

depois disso, mostre a listagem de números gerados e também indique o menor e o maior 
valor que estão na tupla.

"""
import random

num  = (random.randint(0, 60),
        random.randint(0, 60),
        random.randint(0, 60),
        random.randint(0, 60), 
        random.randint(0, 60))

i = maior = menor = 0

print(num)      # mostra os numeros sorteados na tela 


for pos, i in enumerate(num): # começa a contar a posição e os elementos
    
    if pos == 0: 
    # se for a primeira vez que o programa está rodando, pega o 
    # primeiro elemento e define como mair e menor
        maior = i
        menor = i
    
    if i > maior:
        maior = i
    
    if i < menor :
        menor = i

print(f'O maior número sorteado foi´{maior} e o menor foi {menor}')


