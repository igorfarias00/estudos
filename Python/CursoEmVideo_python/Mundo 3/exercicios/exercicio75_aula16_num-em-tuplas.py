# -*- coding: utf-8 -*-
"""
crie um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. no final, 
mostre:
    A) quantas vezes apareceu o valor 9
    B) em que posição foi digitado o primeiro valor 3
    C) quais foram os numeros pares
"""


num = (int(input('Digite um número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite o ultimo número: '))
       )

c = nove = i = tres_pos = 0


print(f'voce digitou:  {num}')


for c in num:
    if c == 9:
        nove += 1
        


#------------------------------------------------------------
while tres_pos == 0 and i < len(num):
    if num[i] == 3:
        tres_pos = i + 1
    i +=1 

# resolução video
print(' o valor 3 apareceu na posição {num.index(3)}')
# -----------------------------------------------------------



print(f'O número Nove apareceu {nove}')

# resolução video
print(' o valor 9 apareceu {num.count(9)} vezes')




if tres_pos != 0:
    print(f'O número três apareceu primeiro na {tres_pos} posição')
else: 
    print('O número três não apareceu. ')
    


    
print('Os números pares foram:')
for c in num:
    if c % 2 == 0:
        print(c, end=' -> ')

