# -*- coding: utf-8 -*-
"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acorde 
com sua idade: 
    
    -se ele ainda vai se alistar ao serviço militar
    -se é a hora de se alistar
    -se já passou do tempo do alistamento
    
seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

"""
from datetime import date

#----------------------------------------------------------------------

birthday = int(input('Qual o ano do seu nascimento?  '))

this_year = date.today().year

age = this_year - birthday

if age < 18:
  
    print('Ainda falta {} ano(s) para se alistar.'.format(18 - age))
    
elif age == 18:
    print('Está na HORA DE SE ALISTAR, VOCE VAI PODER ANDAR DE BARCO, DAR TIRO DE FUZIL')

else:
    print('Ja passou em {} anos do prazo de se alistar, vai pagar a multa.'.format(age - 18))