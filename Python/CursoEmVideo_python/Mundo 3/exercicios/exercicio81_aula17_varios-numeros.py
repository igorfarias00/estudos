# -*- coding: utf-8 -*-
"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
    A) quantos números foram digitados.
    B) A lista de valores, ordenada de forma decrescente
    C) se o valor 5 foi digitado e está ou não na lista
"""
numeros = []
tot_num = 0 
resp = 's'

while True:
    if resp == 'N':
        break
    
    num = int(input('Digite um número: '))
    
    tot_num += 1
    numeros.append(num)
    
    resp = str(input('Deseja continuar?[S/N]')).strip().upper()    

 

print(f'Foram digitados {tot_num} números ao total')
print('A lista dos valores em ordem decrescente é: ')

numeros.sort(reverse=True)
print(numeros)


if 5 in numeros:
    print('O valor 5 foi digitado e está na lista')
    
else:
    print('O valor 5 nao foi digitado e não está na lista')