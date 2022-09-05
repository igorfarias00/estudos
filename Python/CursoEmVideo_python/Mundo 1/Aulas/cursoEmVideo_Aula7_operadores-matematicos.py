# -*- coding: utf-8 -*-

'''
precedência de operadores 
1º - ()
2º - **
3º - * / // %
4º - + - 
'''

print(5 + 3 * 2)
print((5 + 3) * 2)

print(3 * 5 + 4 ** 2)
print(3 * (5 + 4) ** 2)


titan = input('qual o seu nome? ')
print('Ola {:¨^20}!'.format(titan))

n1= int(input('Digite um valor: '))
n2= int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2 
dint = n1 // n2
e = n1 ** n2

print('A soma é {}, o produto é {} e a divisao é {:.3f}'.format(s, m, d), end='  ')
print('Divisao inteira {} e potencia {}'.format(dint, e))