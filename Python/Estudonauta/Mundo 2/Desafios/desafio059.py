n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0

while opcao != 5:
    print('''
    [1] - somar
    [2] - multiplicar
    [3] - maior
    [4] - novos números
    [5] - sair do programa
    ''')
    opcao = int(input('Digite a sua opcao: '))

    if opcao == 1:
        soma = n1 + n2
        print('O resultado da soma de {} e {} é: {}'.format(n1, n2, soma))
    elif opcao == 2:
        resultado = n1 * n2
        print('O resultado da multiplicação de {} por {} é: {}'.format(n1, n2, soma))
    elif opcao == 3:
        if n2 < n1:
            print('O maior é o primeiro numero: {}'.format(n1))
        elif n1 < n2:
            print('O maior é o segundo numero: {}'.format(n2))
        else:
            print('Os numeros são iguais!')
    elif opcao == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    else:
        print('Até mais!')
