valorCasa = float(input('Digite o valor de a casa: R$'))
salario = float(input('Digite o seu sálario: R$'))
anos = int(input('Digite em quantos anos pretende pagar: '))

prestacao = valorCasa / (anos * 12)
if prestacao > salario * 0.3:
    print(f'Valor da prestação ficou em R${prestacao:.2f}')
    print('Emprestimo negado')
else:
    print(f'Você terá que pagar R${prestacao:.2f} por mês!')
