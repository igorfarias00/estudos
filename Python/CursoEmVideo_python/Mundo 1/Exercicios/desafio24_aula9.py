# -*- coding: utf-8 -*-

nome = str(input('Digite o nome da sua cidade: '))

div = nome.split()

print('O primeiro nome da sua cidade é {}'.format(div[0]))
print('É santo? {}'.format('santo' in div[0]))