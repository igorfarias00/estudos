n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

if n1 > n2 and n1 > n3:
    print(f'O maior numero é o n1: {n1}')
else:
    if n2 > n1 and n2 > n3:
        print(f'O maior é n2: {n2}')
    else:
        print(f'O maior é n3: {n3}')

if n1 < n2 and n1 < n3:
    print(f'O menor numero é o n1: {n1}')
else:
    if n2 < n1 and n2 < n3:
        print(f'O menor é n2: {n2}')
    else:
        print(f'O menor é n3: {n3}')
