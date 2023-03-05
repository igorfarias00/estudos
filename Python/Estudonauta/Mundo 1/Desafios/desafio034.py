salario = float(input('Digite o seu salario: '))

if salario > 1250.0:
    salario += salario * 0.10
else:
    salario += salario * 0.15

print(f'O seu novo salário é de R${salario}')
