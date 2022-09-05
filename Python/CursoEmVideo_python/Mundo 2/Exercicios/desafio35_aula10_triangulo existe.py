# -*- coding: utf-8 -*-

reta1 = float(input('Digite a primeira reta: '))
reta2 = float(input('Digite a segunda reta: '))
reta3 = float(input('Digite a terceira reta: '))


if (reta2 - reta3 * 1) < reta1 < (reta2 + reta3):          # |b - c| < a < b + c 
    if (reta1 - reta3 * 1) < reta2 < (reta1 + reta3):      #|a - c| < b < a + c 
        if (reta1 - reta2 * 1) < reta3 < (reta1 + reta2):  #|a - b| < c < a + b 
            print('O triângulo Existe')
        else:
            print('Triângulo não existe')
    else:
        print('Triângulo não existe')
else:
    print('Triângulo não existe') 