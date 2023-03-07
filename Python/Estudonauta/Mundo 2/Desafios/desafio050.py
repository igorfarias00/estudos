pares = soma = 0
for c in range(0, 6):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        soma += num
        pares += 1

print('A soma dos numeros pares digitados é de: {}'.format(soma))
print('E foram encontrados {} números pares. '.format(pares))