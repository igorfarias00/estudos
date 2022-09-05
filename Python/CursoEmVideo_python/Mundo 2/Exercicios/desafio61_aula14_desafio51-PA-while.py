# -*- coding: utf-8 -*-
"""
refaça o desafio51, lendo o primeiro termo e a razão de uma P.A., mostrando os 10 primeiros 
termos da progressão usando a estrutura while

desafio 51 ------------------------------------------------------------------------
termo = int(input('Digite o primeiro termo da Progressão aritimética: '))
razao = int(input('Digite a razão da progressão: '))

decimo = termo + (10 - 1) * razao
 
for c in range(termo, decimo + razao, razao):
    print(c, end=' -> ')
    
-------------------------------------------------------------------------------------
    
"""

termo = int(input('Digite o primeiro termo da progressão aritimética: '))
razao = int(input('Digite a razão da progressão: '))
c = termo

decimo = termo + (10 -1) * razao

while c != decimo + razao:
    print(c , end=' -> ')
    c += razao

    