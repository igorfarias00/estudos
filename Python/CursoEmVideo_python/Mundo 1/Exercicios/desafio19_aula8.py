# -*- coding: utf-8 -*-
import random

aluno1 = str(input('Digite o Nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))

sorteio = random.choice([aluno1, aluno2, aluno3, aluno4])

print('O aluno sorteado foi o/a:  {}'.format(sorteio))