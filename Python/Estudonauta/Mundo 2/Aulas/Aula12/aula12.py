nome = input('Qual o seu nome? ')

if nome.upper() == 'IGOR':
    print('Que nome bonito!')
elif nome.lower() == 'joão' or nome.lower() == 'maria' or nome.lower() == 'paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('O seu nome é bem normal!')
print('Tenha um bom dia, {}'.format(nome))