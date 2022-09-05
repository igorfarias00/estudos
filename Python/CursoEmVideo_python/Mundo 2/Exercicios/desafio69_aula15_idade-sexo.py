# -*- coding: utf-8 -*-
"""
Crie um programa que leia a idade e sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
    A) quantas pessoas tem mais de 18 anos
    B) quantos homens foram cadastrados
    C) quantas mulheres tem menos de 20 anos
    
"""
ent = ''
mulhermenos20 = demaior = homem = 0

print('-' *10 ,'Cadastro de pessoas')
print('-><' * 15)
while True:
    
    if ent == 'N':
        break
    
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa[masculino/feminino]: ')).lower()
    
    if idade > 18:
        demaior += 1
    if sexo =='masculino':
        homem += 1
    if sexo == 'feminino' and idade < 20:    
        mulhermenos20 += 1
    

    ent = str(input('Deseja continuar?[S/N]: ')).upper()

print(f'No total, foram digitados {demaior} pessoas maiores de 18 anos')
print(f'Foram cadastrados {homem} homens.')
print(f'Há no total, {mulhermenos20} mulheres menores de 20 anos')