# -*- coding: utf-8 -*-

import math

cat_oposto = float(input('Digite o cateto oposto: '))
cat_adjace = float(input('Digite o cateto adjacente: '))

hipot = math.hypot(cat_oposto, cat_adjace)

print('A hipotenusa é {:.2f}'.format(hipot))