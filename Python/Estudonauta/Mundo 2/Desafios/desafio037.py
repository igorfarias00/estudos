num = int(input('Digite um numero: '))

opcao = int(input('''
Digite uma opcao:
1 - para conversão para binario
2 - para conversão para octal
3 - para conversão para hexadecimal
'''))

if opcao == 1:
    print('O valor {} em binario: {}'.format(num, bin(num)))
elif opcao == 2:
    print('O valor {} em octal: {}'.format(num, oct(num)))
elif opcao == 3:
    print('O valor {} em hexadecimal: {}'.format(num, hex(num)))
