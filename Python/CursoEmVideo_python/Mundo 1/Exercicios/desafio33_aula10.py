# -*- coding: utf-8 -*-

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite mais um numero: '))

#1  ------------------------------------------------------
if n1 > n2 and n1 >n3 :
    print('O maior numero é {}'.format(n1))
elif  n2 > n1 and n2 > n3:
    print('O maior numero é {}'.format(n2))
else: 
    print('O maior numero é {}'.format(n3))


#2 ---------------------------------------------------    
if n1 < n2 and n1 < n3:
    print('O menor numero é {}'.format(n1))
elif n2 < n1 and n2 < n3:
    print('O menor numero é {}'.format(n2))
else:
    print('O menor numero é {}'.format(n3))