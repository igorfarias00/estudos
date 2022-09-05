# -*- coding: utf-8 -*-
"""
laço c no intervalo (1, 10)
    paso
pega

for c in range (1, 10):
    paso
pega


for c in range (1, 10):
    paso
    pula
paso
pega


for c in range (1, 10):
    se moeda
        pega
    paso
    pula
paso
pega


"""



for c in range (1, 3):
    print('oi')
    
for c in range (1, 10, 2):
    print(c)
    
for c in range (10, 1, -1):
    print(c)

for c in range (10, 0, -1):
    print(c)


n = int(input('Digite um numero: '))

for c in range(0, n+1):
    print(c)
print('fimmmm')


i = int(input('Digite o inicio do indice: '))
f = int(input('digite o fim: '))
p = int(input('Digite o passo: '))

for c in range (i, f+1, p):
    print('OIEE LINDA')
print('fIMM')

s = 0

for c in range (0 , 3):
    n = int(input('Digite um numero: '))
    s += n
print(' O somatorio de todos os numeros foi {}'.format(s))

















