# -*- coding: utf-8 -*-
"""
'''crie um programa que leia a data de nascimento de 7 pessoas e diga se elas 
já são maiores de idade
"""

from datetime import date

nasc = {}                       #array?
data_atual = date.today()       #importa a data atual    

maior = 0
menor = 0

for c in range(0, 7):           #loop para pegar os dados
    nasc[c] = int(input('Digite a data do seu nascimento da {} pessoa: '.format(c+1)))

for c in range(0, 7):           #loop para mostrar os maiores de idade
    if data_atual.year - nasc[c] >= 18:     #testa se é maior de idade
        print('a pessoa {} É maior de idade!!eeeeeh, vai ser preso'.format(c))
        maior += 1
    else: 
        print('pessoa {}, VOCÊ é MULEKE'.format(c))
        menor += 1
        
print('São {} maiores e {} menores de idade'.format(maior, menor))