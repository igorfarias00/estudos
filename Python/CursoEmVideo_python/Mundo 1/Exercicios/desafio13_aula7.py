# -*- coding: utf-8 -*-

salario = float(input('Digite o salario: '))
aumento = float(input('Digite a porcentagem de aumento do salario: '))

valor_final = salario + (salario * (aumento / 100))

print('Parabens, o seu salario com o aumento ficou em R${:.2f}'.format(valor_final))