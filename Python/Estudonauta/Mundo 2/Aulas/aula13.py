'''
moeda = False

for c in range(0, 4):
    print("anda")
    print("Pula")

print("Passo")
print('Pega')
'''

for c in range(0, 6):
    print('Oi')
print('FIM')

for c in range(0, 6):
    print('Oi')
    print('FIM')

for c in range(0, 6):
    print(c)
print('FIM')

for c in range(6, 0, -1):
    print(c)

for c in range(0, 7, 2):
    print(c)

f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))

for c in range(0, f + 1, p):
    print(c)
