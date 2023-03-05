a = float(input('Digite o valor do primeiro lado: '))
b = float(input('Digite o segundo valor: '))
c = float(input('Digite o terceiro valor: '))

if a < b + c and b < a + c and c < a + b:
    print('O triangulo pode ser formado! ')
    if a == b == c:
        print('O triangulo é Equilátero!')
    elif (a == (b or c)) or (b == (c or a)) or (c == (b or a)):
        print('O triangulo é isósceles!')
    else:
        print('é um Triangulo escaleno!')
else:
    print('O triangulo não existe!')
