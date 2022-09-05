# -*- coding: utf-8 -*-
"""
lanche = ('oi', 'ola')  #tupla
lanche = ['oi', 'ola']  #lista
"""

lanche = ['hamburguer', 'suco', 'pizza', 'pudim']

print(lanche[3])

lanche[3] = 'sorvete' # as listas são mutaveis

print(lanche[3])

lanche.append('cookie') # adiciona um elemento no final da lista

print(lanche[4])

lanche.insert(0,'cachorro-quente') 
# insere um elemento na posição especificada e desloca todos os elementos ]
#da lista em uma casa

print(lanche[0])

del lanche[3] # apaga o elemento dentro da posição especificada
# lanche.pop(3) #tambem apaga
# lanche.remove('pizza') # tambem apaga, mas procura o elemento dentro da listae 
#excluia a posição e reposiciona os elementos na lista

if 'pizza' in lanche:
    lanche.remove('pizza')
    
print(lanche)


valores = list(range(4,11))

print(valores)

#---------------pratica ----------------

num = [2, 5, 9, 1]
#num[2] = 3
#num[4] = 7
num.append(7)
#num.sort()
num.sort(reverse=True)
num.insert(2, 0)
num.remove(2)
#num.remove(4)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o numero 4')
#num.pop()
#num.pop(2)

print(num)
print(f'Essa lista tem {len(num)} elementos')

#------------
valores = []

valores.append(5)
valores.append(9)
valores.append(4)

for cont in range(0, 5):
    valores.append(int(input('Digite um numero: ')))

"""for v in valores:
    print(f'{v}...', end='')
"""
    
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('cheguei ao final da lista')
#------
a = [2, 4, 5, 6]
b = a

print(a)
print(b)






    
