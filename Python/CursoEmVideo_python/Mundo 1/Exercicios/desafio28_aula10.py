# -*- coding: utf-8 -*-
import random

escol = int(input('Digite o seu palpite: '))

sort = random.randint(1 , 5)

if sort == escol:
    print('PARABENS, acertou o numero sorteado.')
else:
    print('TENTE OUTRA VEZ... numero sorteado foi {}'.format(sort))