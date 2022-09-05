# -*- coding: utf-8 -*-
"""
''' crie um programa que leia uma frase e diga se  ela é  um palindromo'''
"""

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()            # divide as palavras da frase
frase = ''.join(palavras)           #junta tudo denovo sem os espaços



inverso = ''

tam = int(len(frase))


for c in range(tam - 1, -1, -1):    # inverte a frase na variavel inverso
    inverso += frase[c]
    



print('\n O inverso de "', frase, '"   é  --', inverso, '-- ')
    
if inverso == frase:                #se a frase for igual ao inverso é um palindromo
    print('A frase é um palindromo')
else:
    print('A frase não é um palindromo')
