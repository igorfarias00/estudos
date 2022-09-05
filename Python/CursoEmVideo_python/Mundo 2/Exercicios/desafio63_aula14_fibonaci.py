# -*- coding: utf-8 -*-
"""
escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros 
elementos de uma sequencia de fibonacci..

"""
print('Sequência de fibonacci #------------------')

n = int(input('Digite o número de termos que você quer ver: '))

i = 1
anterior = 0
fib = 1
aux = 0

while i != n:               #enquanto o laço nao atingir o numero de termos solicitado
    fib = aux + fib         # fibonacci  recebe o valor do termo anterior salvo na variavel 
                            #auxiliar aux e o termo corrente
    aux = anterior          # salva o termo anterior na auxiliar
    anterior = fib          # atualiza o termo atual
    
    
    
    print(fib, end=' -> ')
    i += 1
    