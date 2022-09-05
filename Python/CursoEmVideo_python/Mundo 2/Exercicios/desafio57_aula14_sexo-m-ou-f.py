# -*- coding: utf-8 -*-
"""
faça um programa que leia o sexo de uma pessoa , mas só aceite os valores 'M' ou 'f'.
caso esteja errado, peça a digitação novamente até ter um valor correto.

"""
sex = ''

while sex != 'm' and sex != 'f':
    sex = str(input('Digite o seu sexo[m/f]: ')).lower()
    
    if sex != 'm' and sex != 'f':
        print('Entrada inválida, digite novamente \n')

print('Registrado com sucesso')  # resolução do video 

print('fim!')