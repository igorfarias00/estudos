# -*- coding: utf-8 -*-
"""
crie um programa com uma tupla preenchida com os 20 primeiros colocados do Campeonato
Brasileiro de Futebol, na ordem de colocação. Depois mostre:
    A) apenas os 5 primeiros colocados.
    B) os últimos 4 colocados da tabela
    C) Uma lista com os times em ordem alfabética 
    D) Em que posição da tabela esta o time chapecoense

"""

times = ('flamengo', 'internacional','atletico-mg','sao paulo', 'fluminense',
         'gremio', 'palmeiras','santos', 'athletico-pr', 'bragantino','ceará',
         'corinthians', 'atletico-go', 'bahia', 'sport', 'fortaleza', 'vasco',
         'goias', 'coritiba', 'botafogo')

c = achou = pos = i = 0

ultimos4 = len(times) - 4

#AAAAAA------------------------------------------------------------
while i < 5:
    print(times[i])
    i += 1
print('=' * 20)

#resolução video--#####
print('#' * 20)
print(f'Os 5 primeiros são {times[0:5]}')

print('#' * 20)

#BBBBBB------------------------------------------------------------------
while ultimos4 < len(times):
    print(times[ultimos4])
    ultimos4 += 1
print('='*20)

#resolução video--#####
print('#' * 20)
print(f'Os 4 Ultimos são {times[-4:]}')

print('#' * 20)

#CCCCCC----------------------------------------------------------------


print(sorted(times)) # igual a resolução
print('='*20)



#DDDDDD---------------------------------------------------------------
for pos , c in enumerate(times):        #procura a chapecoense na tupla
    if c == 'chapecoense':              #se achou mostra a posição na tabela e o nome
        print(pos+1, c)
        achou = 1
    elif pos == len(times) - 1 and achou != 1:  
        # se nao printa só depois que percorrer toda a tabel
        print('A chapecoense nao está nesse brasileirão')
print('='* 20)



"""#resolução video--#####
print('#' * 20)
print(f'O chapecoense está na {times.index("chapecoense")+1} posição') # funcionaria se a chapecoense existise na tupla

print('#' * 20)
"""
