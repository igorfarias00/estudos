# -*- coding: utf-8 -*-

dist = float(input('Digite a distância: '))

if dist <= 200:
    total = dist * 0.50
else:
    total = dist * 0.45
    
print('O total da viagem é de: {:.2f}'.format(total))
