distancia = float(input('Digite a distancia da viagem: '))

if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45

print(f'O valor total da pasagem é de R${valor}')
