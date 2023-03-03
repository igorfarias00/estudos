import math

angulo = float(input('Digite um ângulo qualquer(em radianos): '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'O seno vale: {seno}')
print(f'O cosseno vale: {cosseno}')
print(f'A tangente vale: {tangente}')
