# -*- coding: utf-8 -*-
dias = int(input('Por quantos dias o carro foi alugado? '))
kms = float(input('Por quantos quilometros? '))

valor = dias * 60.00 + kms * 0.15

print('O valor do aluguel foi de R${:.2f}'.format(valor))