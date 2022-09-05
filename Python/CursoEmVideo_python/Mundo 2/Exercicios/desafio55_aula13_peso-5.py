# -*- coding: utf-8 -*-
"""
'''leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lido'''
"""
peso = {}
maior = 0
menor = 9999


for c in range(0, 5):
    peso[c] = float(input('Digite o seu peso: '))
    if peso[c] > maior:
        maior = peso[c]
    elif peso[c] < menor:
        menor = peso[c]

print('O maior peso foi: {}kg'.format(maior))
print('O menor peso foi: {}kg'.format(menor))



# solução do video ----------------------------------------------------------

for c in range(1, 6):
    peso = float(input('Digite o seu peso: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
            