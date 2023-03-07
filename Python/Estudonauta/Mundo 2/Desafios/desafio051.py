termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digita a razão da P.A.: '))
i = 1
for c in range(termo, razao * 11, razao):
    print('{}º termo: {}'.format(i, c))
    i += 1
