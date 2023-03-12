razao = int(input('Digite a razao: '))
primeiroTermo = int(input('Digite o primeiro termo: '))
fim = primeiroTermo
continuar = 's'

while continuar == 's':
    termo = fim // razao
    print('termo {}: {}'.format(termo, fim))
    fim += razao
    continuar = input('Gostaria de continuar? s | n: ').lower()
