tempo = int(input('Digite quantos anos tem o seu carro: '))

if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho!')

print('Carro novinho' if tempo <= 3 else 'LATA VEIA!')

nome = str(input('Digite o seu nome: '))

if nome == 'Gustava':
    print('Que nome lindo vocÊ tem!')
else:
    print('Seu nome é tão normal...')

print(f'Bom dia, {nome}!')


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda note: '))

media = (n1 + n2) / 2

print(f'A sua média foi {media}')
if media >= 6.0:
    print('A sua media foi boa! para bens!')
else:
    print('Sua média foi ruim! ESTUDE MAIS')

print('PARABENNS!' if media >= 6.0 else 'ESTUDE MAIS')