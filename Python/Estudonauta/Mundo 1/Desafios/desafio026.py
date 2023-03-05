frase = input('Digite uma frase: ').strip()

print(f'A letra "A" aparece {frase.upper().count("A")} vezes')
print(f'A primeira vez que ela aparece é na posição {frase.upper().find("A")}')
print(f'E a ultima vez que ela aparece é na posição {frase.upper().rfind("A")}')