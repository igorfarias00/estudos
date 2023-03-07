for c in range(0, 5):
    peso = float(input('Digite um peso: '))
    if c == 0:
        maior = peso
        menor = peso
    elif maior < peso:
        maior = peso
    if menor > peso:
        menor = peso

print('O maior peso foi {} e o menor peso foi {}'.format(maior, menor))