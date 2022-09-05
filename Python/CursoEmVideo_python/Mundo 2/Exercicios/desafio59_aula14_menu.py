# -*- coding: utf-8 -*-
"""
crie um programa que leia dois valores e mostre na tela um menu:
    [1] - somar
    [2] - multiplicar
    [3] - maior 
    [4] - novos números 
    [5] - sair do programa
    
seu programa deverá realizar a operação solicitada em cada caso

"""

opcao = 0

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

while opcao != 5:
    print("""
          [1] - somar
          [2] - multiplicar
          [3] - maior
          [4] - novos números
          [5] - sair do programa""")

    opcao = int(input('Digite a opção: '))
    
    if opcao == 1:
        print('A soma dos numeros é {}'.format(n1 + n2))
        opcao = 0
    
    
    elif opcao == 2:
        print('A multiplicação de {} por {} é {}'.format(n1, n2, n1 * n2))
        opcao = 0
    
    
    elif opcao == 3:
        if n1 > n2:
            print(n1, ' é maior que ', n2)
        elif n2 > n1:
            print(n2, ' é maior que ', n1)
        else:
            print('Os dois numeros são iguais')
        opcao = 0
    
    
    elif opcao == 4:
        n1 = int(input('Digite um novo numero: '))
        n2 = int(input('Digite outro novo numero: '))
        opcao = 0    
            
            
    
        
        
        