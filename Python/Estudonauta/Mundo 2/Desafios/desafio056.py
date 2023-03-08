mulheresMenorDeVint = media = 0
for c in range(0,3):
    nome = input('Digite o seu nome: ')
    idade = int(input('Digite a sua idade: '))
    sexo = input('Digite o seu sexo( m - masculino | f - feminino) : ').lower()

    if c == 0:
        maisVelhoNome = nome
        maisVelhoIdade = idade
        if sexo == 'm':
            maisVelhoMasculino = True
        else:
            maisVelhoMasculino = False

    elif maisVelhoIdade <= idade and sexo == 'm':
        maisVelhoNome = nome
        maisVelhoIdade = idade

    if sexo == 'f' and idade < 20:
        mulheresMenorDeVint += 1

    media += idade

media /= 3

print('A idade media do grupo: {}'.format(media))
print('Mulheres com menos de 20 anos: {}'.format(mulheresMenorDeVint))
if maisVelhoMasculino:
    print('O home mais velho: {}'.format(maisVelhoNome))
else:
    print('Nao foram inseridos homens')