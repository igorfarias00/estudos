import random

aluno1 = input('Digite o nome dos alunos: ')
aluno2 = input('Digite o nome de outro aluno: ')
aluno3 = input('Digite o nome de mais um aluno: ')
aluno4 = input('Digite o nome do ultimo aluno: ')

sorteado = random.choice((aluno1, aluno2, aluno3, aluno4))

print(f'O aluno sorteado foi o {sorteado}')
