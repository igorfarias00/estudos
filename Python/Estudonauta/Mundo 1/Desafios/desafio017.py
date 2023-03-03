import math

oposto = float(input('Digite o comprimento do cateto oposto: '))
adjacente = float(input('Digite o comprimetno do cateto adjacente: '))

hipotenusa = math.sqrt(pow (oposto, 2) + pow(adjacente, 2))

hipot = math.hypot(oposto, adjacente)

print(f'A hipotenusa vale {hipotenusa:}')
print(f'A hipotenusa pela biblioteca é {hipot}')