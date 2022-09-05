# -*- coding: utf-8 -*-
"""
melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
o programa encerra quando ele disser que quer mostrar 0 termos.

termo = int(input('Digite o primeiro termo da progressão aritimética: '))
razao = int(input('Digite a razão da progressão: '))
c = termo

decimo = termo + (10 -1) * razao

while c != decimo + razao:
    print(c , end=' -> ')
    c += razao
 
"""

termo = int(input('Digite o primeiro termo da progressão aritimética: '))
razao = int(input('Digite a razão da progressão: '))
quant_termo = int(input('Quantos termos voce quer mostrar na tela? '))
                  
c = termo
final = termo + (quant_termo - 1) * razao

while quant_termo != 0:
    final = termo + (quant_termo - 1) * razao
    c = termo
    while c != final + razao: 
        print(c, end=' -> ')
        c += razao
    quant_termo = int(input('quer mostrar mais alguns termos na tela?digite quantos deseja: '))
    
