# -*- coding: utf-8 -*-

nome = str(input('Digite seu nome: '))

print(nome.upper())   #1

print(nome.lower())   #2



dividida = nome.split()
tudojunto =  ''.join(dividida)

print(len(tudojunto))     #3

print(len(dividida[0]))   #4

