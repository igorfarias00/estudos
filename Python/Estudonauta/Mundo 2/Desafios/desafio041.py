from datetime import date

nasc = int(input('Digite o ano do seu nascimento: '))
nasc = date.today().year - nasc

if nasc <= 9:
    print('MIRIM')
elif nasc <= 14:
    print('INFANTIL')
elif nasc <= 19:
    print('Junior')
elif nasc <= 20:
    print('SÊNIOR')
else:
    print('MASTER')