# -*- coding: utf-8 -*-

frase = 'Curso em Video Python'

print(frase[9])
print(frase[9:13])
print(frase[9:14])
print(frase[9:21])   # inicio:fim:Pulandoelementos
print(frase[9:21:2]) # inicio:fim:Pulandoelementos
print(frase[:5])
print(frase[15:])
print(frase[9::3])

print(len(frase))
print(frase.count('o')) # contagem do elemento na frase
print(frase.count('o', 0 , 13)) # contagem do caractere com fatiamento

print(frase.find('deo'))   #acha a pesquisa na frase
print(frase.find('Android'))
print(('curso' in frase))

print(frase.replace('Python', 'Android'))

print(frase.upper())  #trasforma minuscula em maiuscula
print(frase.lower())  #trasforma maiuscula em minuscula

print(frase.capitalize())  #deixa so a primeira letra em maiuscula

print(frase.title())  # deixa a primeira letra de cada palavra em maiuscula



frase2 = '   Aprenda Python  ' 

print(frase2.strip())# remove os espaços vazio antes e depois da frase
print(frase2.rstrip())  #remove os espaços somente a direita
print(frase2.lstrip())  #remove os espaços somente a esquerda


frase = frase.split() # explode a string em outras strings, fica dentro de uma lista
frase = '-'.join(frase)         #junta a frase denovo
print(frase)

