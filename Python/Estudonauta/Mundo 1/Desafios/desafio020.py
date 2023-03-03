import random

aluno1 = input('Digite o nome dos alunos: ')
aluno2 = input('Digite o nome de outro aluno: ')
aluno3 = input('Digite o nome de mais um aluno: ')
aluno4 = input('Digite o nome do ultimo aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)

print(f'O primeiro aluno é o: {lista[0]}')
print(f'O segundo aluno é o: {lista[1]}')
print(f'O terceiro aluno é o: {lista[2]}')
print(f'O ultimo aluno é o: {lista[3]}')

