# -*- coding: utf-8 -*-
"""
'''faça um programaque calcule a soma entre todos os números ímpares que são
múltiplos de três e que se encontram no intervalo de 1 até 500  '''

"""
soma = 0
i=0



for c in range(1, 501, 2):  #percorre o intervalo pulando de 2 em 2
    if  c % 3 ==0:          # se o resultado da divisao por for igual a zero
        
        print('\033[1;33;44m', c, end=' ')
        soma += c
        i += 1


print('A soma de todos os {} numeros foi de {}' .format(i, soma))