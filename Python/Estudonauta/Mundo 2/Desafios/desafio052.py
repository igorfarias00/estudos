num = int(input('Digite um numero: '))
divisores = 0

for c in range(1, num+1):
    if num % c == 0:
        divisores += 1

if divisores > 2:
    print('Não é um numero primo!')
else:
    print('É um numero primo!')