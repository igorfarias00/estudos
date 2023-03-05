from datetime import date as dt
ano = int(input('Digite o ano ou digite 0 para pegar o ano atual: '))

if ano == 0:
    ano = int(dt.today().year)

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('é Bissexto')
else:
    print('NÃO é BISSEXTO!')
