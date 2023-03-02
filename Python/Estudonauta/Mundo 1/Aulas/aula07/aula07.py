n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {} \nO produto é {} \ne a divisão é {:.3f}\n'.format(s, m, d), end='>>>')
print('A divisao inteira {}\n e a potencia {}'.format(di, e))


