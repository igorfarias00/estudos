from datetime import date

maiores = menores = 0

for c in range(0, 6):
    ano = int(input('Digite o seu ano de nascimento: '))
    idade = date.today().year - ano
    if idade >= 21:
        maiores += 1
    elif idade >= 0:
        menores += 1

print('Há {} maiores de idade e {} menores de idade!'.format(maiores, menores))
