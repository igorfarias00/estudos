sexo = ''
while sexo != 'm' and sexo != 'f':
    sexo = input('Digite um sexo:').lower()
    if sexo != 'm' and sexo != 'f':
        print('Sexo invalido, digite novamente!')
