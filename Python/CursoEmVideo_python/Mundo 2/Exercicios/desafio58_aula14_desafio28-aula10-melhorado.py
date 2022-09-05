# -*- coding: utf-8 -*-
"""
melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só
que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram 
necessários para vencer.

desafio 28-------------0---------------------

import random

escol = int(input('Digite o seu palpite: '))

sort = random.randint(1 , 5)

if sort == escol:
    print('PARABENS, acertou o numero sorteado.')
else:
    print('TENTE OUTRA VEZ... numero sorteado foi {}'.format(sort))
    
-------------0------------------------------------

 
"""
import random

sort = random.randint(0, 10)
tenta = 0
jogador = 0

print('----- # JOGO DA ADIVINHAÇÃO  # ------------------')

while jogador != sort:
    jogador = int(input('Digite seu palpite:  '))
    
    if jogador != sort:
        print('VOCÊ NÃO ACERTOU, TENTE OUTRA VEZ...')
        tenta += 1

print('Parabéns, Você acertou. só custou {} tentativas'.format(tenta))

