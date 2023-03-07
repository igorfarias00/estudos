num = int(input('Digite um numero: '))
print(20*'=')
for c in range(0, 11):
    print('{:^3} x {:^} = {:^}'.format(c, num, num * c))

