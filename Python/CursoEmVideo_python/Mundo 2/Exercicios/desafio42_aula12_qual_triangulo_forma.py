# -*- coding: utf-8 -*-
"""
Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
será formado:
    
    -Equilátero: todos os lados iguais 
    
    -Isósceles: dois lados iguais
    
    -Escaleno: todos os lados diferentes
"""

a = float(input('Digite a primeira Reta: '))  
b = float(input('Digite a segunda reta: '))
c = float(input('Digite a terceira reta: '))

if (b - c) < a < b + c:             # |b - c| < a < b + c 
    if (a - c) < b < a + c:         #|a - c| < b < a + c 
        if(a - b) < c < a + b:      #|a - b| < c < a + b 
            print('O Triângulo existe')
            if a == b == c:
                print('É UM TRIÂNGULO EQUILATERO!')
            elif a != b and a != c and b != c:
                print('È UM TRIÂNGULO Escaleno!!')
            else:
                print('É UM TRIÂNGULO ISóSCELES')
            
            
            
        else: 
            print('O triângulo não existe!')
    else:
        print('O triângulo não existe!')
else:
    print('O triângulo não existe!')