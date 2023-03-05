import random
from time import sleep
sorteado = random.randrange(0, 5)

palpite = int(input('Tente adivinhar o numero: '))
print('PROCESSANDO...')
sleep(2)
print('ACERTOU' if palpite == sorteado else 'ERROW')
