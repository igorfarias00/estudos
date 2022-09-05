# -*- coding: utf-8 -*-

preco = float(input('Digite o valor: '))
desconto = float(input('Digite o valor da porcentagem de desconto(%): '))

valor = preco - (preco * (desconto / 100))

print('O preco com o desconde é de R${:.2f}'.format(valor))