from random import randrange

maquina = randrange(0, 10)
jogador = -1
palpites = 0

while jogador != maquina:
    print('\033[1:31:46m=+' * 20 + '\033[0:0:0m')
    jogador = int(input('Digite o seu palpite: '))
    print('\033[1:31:46m=+' * 20 + '\033[0:0:0m')
    if jogador == maquina:
        print('Acertou, você ganhou')
        print('Foram necessarios {} palpites.'.format(palpites))
    else:
        print('ErrouW! tente novamente')
        palpites += 1

