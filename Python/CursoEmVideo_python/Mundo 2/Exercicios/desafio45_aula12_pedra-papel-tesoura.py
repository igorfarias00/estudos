# -*- coding: utf-8 -*-
"""
Crie um programa que faça o computador jogar jokenpô com você

"""

import random

print('qual a sua jogada? ')

player = int(input('1 - Pedra | 2 - Tesoura | 3 - Papel |  '))

npc = random.randint(1,3)

iten = ('pedra', 'tesoura', 'papel')

if player == npc:
    print('Empate, Jogue novamente')
elif (player == 1 and npc == 2) or ( player == 2 and npc == 3 ) or ( player == 3 and npc == 1 ):
    print('Você venceu!!!')
    print('O jogador jogou {}'.format(iten[player]))
    print('O computador jogou {}'.format(iten[npc]))
else:
    print('O Computador venceu, você perdeu, SEU ARROMBADO')
    print('O jogador jogou {}'.format(iten[player-1]))
    print('O computador jogou {}'.format(iten[npc-1]))
    