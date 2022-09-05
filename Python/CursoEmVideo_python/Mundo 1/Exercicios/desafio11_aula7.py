# -*- coding: utf-8 -*-

larg = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area_parede = larg * altura

litro_tinta = area_parede / 2

print('Será necessario {:.2f} litros de tinta para pintar a parede. Que tem {:.2f}m²'.format(litro_tinta, area_parede))