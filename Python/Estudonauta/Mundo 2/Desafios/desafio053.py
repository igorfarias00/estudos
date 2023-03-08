frase = input("Digite a sua frase: ").lower().strip().split()

print(len(frase))
fraseSem =''
diferente = False

for c in range(0, len(frase)):
    fraseSem += frase[c]
'''print(fraseSem)'''

junto = ''.join(frase)

inverso = frase[::-1]

for c in range(len(fraseSem)-1, -1, -1):
    '''print(c)
    print((len(fraseSem)-1) - c)'''
    if fraseSem[c] != fraseSem[(len(fraseSem)-1) - c]:
        diferente = True

if diferente:
    print('Não é palíndromo')
else:
    print('É PALÍNDROMO!')