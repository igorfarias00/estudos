# -*- coding: utf-8 -*-
import math

num = float(input('Digite um número: '))

print('O número {:.3f} tem a parte inteira de {}.'.format(num, math.trunc(num)))