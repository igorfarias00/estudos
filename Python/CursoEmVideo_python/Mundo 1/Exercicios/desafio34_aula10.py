# -*- coding: utf-8 -*-

salario = float(input('Digite seu salario: '))
novo_sal = 0

if salario > 1250:
    novo_sal = salario + (salario * 10 / 100)
else:
    novo_sal = salario + (salario * 15/ 100)
    
print('PARABENS, O seu novo salario é {:.2f}'.format(novo_sal))