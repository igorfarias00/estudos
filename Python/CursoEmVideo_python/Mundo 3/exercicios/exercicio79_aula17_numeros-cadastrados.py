# -*- coding: utf-8 -*-
"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os
em uma lista. Caso o número já exista lá dentro, ele não será adicionado. 

No final, serãoexibidos todos os valores únicos digitados, em ordem crescente.

"""
numeros = []
choice = 'S'
achou = 0

while True:
    if choice == 'N':
        break
    
    entrada = int(input('Digite um número: '))
    achou = 0    
    
    for c in range(0, len(numeros)):
        if entrada == numeros[c]:
            achou = 1
            
                
    if achou == 1:
        print('Entrada duplicada. o número não será salvo!')
    else:
        numeros.append(entrada)
    
    choice = str(input('Deseja cadastrar outro número?[S/N] ')).strip().upper()
    
print('=*'* 20)
numeros.sort()
print(f'Você digitou os números {numeros}')