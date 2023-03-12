razao = int(input('Digite a razao: '))
primeiroTermo = int(input('Digite o primeiro termo: '))
fim = primeiroTermo

while fim != razao * 11:
    termo = fim // razao
    print('termo {}: {}'.format(termo, fim))
    fim += razao
