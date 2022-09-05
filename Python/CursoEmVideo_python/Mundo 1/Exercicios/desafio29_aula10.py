# -*- coding: utf-8 -*-
v = float(input('Digite a velocidade do carro: '))

if v > 80.0:
    print('FOI MULTADO, SEU IMPRUDENTE')
    multa = (v - 80) * 7
    print('A multa ficou no valor de: {:.2f}'.format(multa))

else:
    print('segue a viagem')
    
