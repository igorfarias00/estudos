# -*- coding: utf-8 -*-
tempo = int(input('Digite quantos anos tem o seu carro: '))


if tempo <= 3 :
    print('Carro novo')
else:
    print('Carro velho em meu filho')

print('FIM!')


print('Carro novo' if tempo<=3 else 'carro velhor')   

#------------------------------------------------------------

nome = str(input('Digite o seu nome: '))

if nome.lower() == 'igor':
    print('Belo nome guerreiro')
else:
    print('que coisa em {}'.format(nome))
    
# --------------------------------------------------------

n1 = float(input('Digite um numero: '))
n2 = float(input('Digite oto numero: '))

m = (n1 + n2) / 2

if m >= 6:
    print('Sua media foi boa, parabens.')
else:
    print('Estude mais na proxima')

    
print('A sua media foi de {:.2f}'.format(m))
