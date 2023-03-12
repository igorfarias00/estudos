n = 1
r = 's'
par = impar = 0

for c in range(1, 10):
    print(c)
print('FIm')

c = 1
while c < 10:
    print(c)
    c += 1
print('FIM while')

while n != 0:
    n = int(input('Digite um valor: '))
print('FIM while com flag')

while r == 's':
    n = int(input('Digite um valor: '))
    r = input('Deseja inserir outro numero? s | n:  ').lower()
print('FIM while com flag')
r = 's'

while r == 's':
    n = int(input('Digite um valor: '))
    r = input('Deseja inserir outro numero? s | n:  ').lower()
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print('Valores pares: {}'.format(par))
print('Valores impares: {}'.format(impar))

print('FIM while com flag| pares e impares')