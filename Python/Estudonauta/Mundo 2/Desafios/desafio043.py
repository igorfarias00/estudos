altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))

imc = peso / altura ** 2

if imc <= 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal!')
elif imc < 30:
    print('SOBREPESO!')
elif imc < 40:
    print('OBESIDADE, CUIDADO!')
else:
    print('OBESIDADE MORBIDA, MEDICO JÁH!')
