# -*- coding: utf-8 -*-
"""
Tuplas 


"""

lanche = ('hamburgur', 'suco', 'pizza', 'pudim')

print(lanche[1])
print(lanche[3])
print(lanche[-2])
print(lanche[1:3])      # desconsidera o ultimo elemento, no caso, 3

print(lanche)

# lanche[1] = 'refrigerante' # o comando está errado, pois tuplas são imutaveis

#for cont in range(0, len(lanche)):
#    print(f'não irei comer {lanche[cont]}')
print('='*20)


for c in lanche:
    print(f'Eu vou comer {c}')
print('Comi para caramba \n')
print('='*20)

for pos, c in enumerate(lanche):
    print(f'Eu vou comer {c} na posição {pos}')
print('Comi em demasia')
print('='*20)

print(sorted(lanche)) # ordena a tupla em uma lista 
print(lanche)

print('='*20)

a = (2, 5, 4)
b = (5, 8, 1, 2)
print(a)
print(b)

c = a + b

print(c)
print(sorted(c))
print(c.count(5))
print(c.count(9))
print(c.index(4))
print('='*20)

pessoa = ('Gustavo', 39, 'masculino', 99.88)
del(pessoa)      #apaga a tupla pesso
#print(pessoa)    # gera o erro de não definição, por que a variavel fui excluido


