# -*- coding: utf-8 -*-
"""
A confederação Nacional de Natação precisa de um programa
que leia o ano de nascimento de um atleta e mostre sua categoria,
 de acordo com a idade:
     -Até 9 anos: Mirim
     -Até 14 anos: Infantil
     -Até 19 anos: Junior
     -Até 20 anos: Sénior
     -Acima: MASTER
     
"""
from datetime import date


birthday = int(input('Em qual ano você nasceu? '))

this_year = date.today()               # puxa a data atual em mes/dia/ano e coloca na variavel como um array 
age = this_year.year - birthday        # faz o calculo para saber a idade 

if age <= 9:
    print('Categoria Mirim')
elif age <= 14 and age > 9:
    print('CATEGORIA INFANTIL')
elif age > 14 and age <= 19:
    print('CATEGORIA JUNIOR')
elif age > 19 and age <= 20:
    print('CATEGORIA SÉNIOR')
elif age > 20:
    print('CATEGORIA MASTER')