# -*- coding: utf-8 -*-
"""

enquanto verdadeiro:
    se bloco:
        passo
    
    se buraco:
        pula
    
    se moeda:
        pega
    
    se trofeu:
        pula
        interrompa
    
pega


while true:
    if bloco:
        passo
    if buraco
        pula
    if moeda:
        pega
    if trofeu:
        pula
        break
pega
"""

cont =1 
while cont <= 10:
    print(cont, ' ', end='')
    cont += 1
print('Acabou')


#loop infinito 
"""
while True:
    print(cont, ' ', end='')
    cont += 1
print('Acabou')
"""

n = s = 0
while n!=999:
    n = int(input('Digite um numero: '))
    s += n
    
print(s)

n = s = 0       # o programa salva os valores do outro laço de repetição, entao precisa zeralos 
while True:
    n = int(input('Digite um numero para somar: '))
    if n == 999:
        break
    s += n

print('A soma foi de {}'.format(s))

print(f'A soma foi de {s}') # pep python 3.6 - fstrings



