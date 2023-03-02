n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
print(type(n1))

print('A soma de {} e {} é {}'.format(n1, n2, n1+n2))

soma = n1 + n2
print('A soma de {} e {} é {}'.format(n1, n2, soma))


bulean = bool(input('Digita alguma coisa, meu consagrado: '))
print(bulean)

testeIsNum = input('Digita mais alguma coisa ai: ')
print(testeIsNum.isnumeric())
print(testeIsNum.isalpha())
print(testeIsNum.isalnum())
print(testeIsNum.isupper())

import sys

x = 10
print(sys.getsizeof(x))

y = 3.14
print(sys.getsizeof(y))

z = True
print(sys.getsizeof(z))

s = 'Hello, World!'
print(sys.getsizeof(s))

n = None
print(sys.getsizeof(n))




