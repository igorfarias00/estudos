nome = input('Digite o seu nome: ')

print(f'MAIUSCULA: {nome.upper()}')
print(f'Minuscula: {nome.lower()}')
print(f'Total de letras: {len(nome) - nome.count(" ")}')

nomes = nome.split()
print(f'Letras no primeiro nome: {len(nomes[0])}')
