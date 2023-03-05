velocidade = float(input('Digite a velocidade do carro: '))

if velocidade > 80.0:
    print('Foi multado, rapá')
    multa = (velocidade - 80.0) * 7.0
    print(f'Vai ter que pagar {multa} reais em multa!')
else:
    print('Boa viagem!')