distancia = float(input('Quantos kms foram percorridos? '))
dias = int(input('O carro foi alugado por quantos dias? '))

total = 0.15 * distancia + 60 * dias

print(f'O total a pagar pelo aluguel do carro é de R${total:.2f}')
