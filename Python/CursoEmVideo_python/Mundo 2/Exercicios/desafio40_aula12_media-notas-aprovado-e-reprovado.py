# -*- coding: utf-8 -*-
"""
Crie um programa que leia duas notas de um aluno e calcule sua média.
Mostrando uma mensagem no final, de acordo com a média atingida:
    -média abaixo de 5.0
    REPROVADO
    
    -média entre 5.0 e 6.9
    RECUPERAÇÃO
    
    -média 7.0 ou superior
    APROVADO
"""
a = float(input('Digite a primeira nota: '))
b = float(input('Digite a segunda nota: '))

mean = (a + b) / 2

if mean < 5:
    print('REPROVADO | nota do aluno: {:.2}'.format(mean))
elif mean >= 5 and mean < 7:
    print('RECUPERAÇÃO | nota do aluno: {:.2}'.format(mean))
elif mean >= 7:
    print('APROVADISSSIMO!!!  |  nota do aluno: {:.2}'.format(mean))

