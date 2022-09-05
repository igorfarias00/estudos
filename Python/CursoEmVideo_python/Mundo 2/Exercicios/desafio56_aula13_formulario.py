# -*- coding: utf-8 -*-
"""

desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre
    - A média de idade do grupo
    - Qual é o nome do homem mais velho.
    - Quantas mulheres têm menos de 20 anos
'''
"""

nome = {}
idade = {}
sexo = {}

media = 0
velho = 0
posvelho = 0
muiemenos20 = 0

for c in range(0, 4):
    print('----------{}ª pessoa ------------'.format(c+1)) # conteudo do video de correção 
    
    nome[c] = str(input('Digite o seu nome: '))
    idade[c] = int(input('Qual a sua idade: ')) 
    sexo[c] = str(input('Qual o seu sexo? ')).lower()
    
    media += idade[c]
    
    if velho < idade[c] and sexo[c] == 'masculino':  # se for o mais velho é do sexo masculino
        velho = idade[c]                            #salva a maior idade
        posvelho = c                                # salva a posição 
        
    if idade[c] < 20 and sexo[c] == 'feminino':    # se for menor de 20 e do sexo feminino
        muiemenos20 += 1                             # conta as mulheres abaixo de 20 anos
 
media = media / 4

print('A média de idade do grupo é: {}'.format(media))

if velho != 0:    
    print('O nome do homem mais velho é: {}'.format(nome[posvelho]))
else:
    print('Não a homens nesta lista')
    
    
    
print('há {} mulheres com menos de 20 anos'.format(muiemenos20))



