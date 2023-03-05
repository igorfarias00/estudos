n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))

media = (n1 + n2) / 2

if media >= 7.0:
    print('APROVADO! parabens. nota: {}'.format(media))
elif media < 5.0:
    print('REPROVADO! nota: {}'.format(media))
else:
    print('Em RECUPERAçÃO! nota: {}'.format(media))