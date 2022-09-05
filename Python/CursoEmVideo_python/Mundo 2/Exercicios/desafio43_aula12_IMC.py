# -*- coding: utf-8 -*-
"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o imc e mostre 
seu status, de acordo com a tabela abaixo:
    
    -Abaixo de 18.5: ABAIXO DO PESO
    
    -Entre 18.5 e 25: PESO IDEAL 
    
    -25 e 30: SOBREPESO
    
    -30  Até 40:OBESIDADE
    
    -Acima de 40: OBESIDADE MÓRBIDA
"""

peso = float(input('Digite seu peso em kg: '))

altura = float(input('Digite sua altura em metros: '))

imc = peso / altura ** 2

if imc < 18.5:
    print('ABAIXO DO PESO, COME!!!')
    
elif imc >= 18.5 and imc < 25:
    print("Peso IDEAL")
    
elif imc >= 25 and imc < 30:
    print('SOBREPESO')
    
elif imc >= 30 and imc < 40:
    print('OBESIDADE')
    
elif imc >= 40:
    print('OBESIDADE MÓRBIDA, GORDAO')