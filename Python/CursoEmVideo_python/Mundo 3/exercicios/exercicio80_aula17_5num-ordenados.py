# -*- coding: utf-8 -*-
"""
Crie um programa onde o usuário possa digitar cinco valores númericos e castre-os em uma
lista, já na posição correta de inserção( sem usar o sort() )

No final, mostre a lista ordenada na tela
"""
num = c = fim_da_lista = fim =0

numeros = []


for c in range(0, 5):
    
    num = int(input('Digite um valor: '))
    
    
    if len(numeros) == 0 :
        numeros.append(num)
        
    elif len(numeros) == 1 and num <= numeros[0]:
        numeros.insert(0, num)
    elif len(numeros) == 1:
        numeros.append(num)
        
    
    
print(numeros)