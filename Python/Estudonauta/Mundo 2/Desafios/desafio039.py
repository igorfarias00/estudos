from datetime import date
nasc = int(input('Digite a sua data de nascimento: '))

if date.today().year - nasc < 18:
    print('Você ainda vai ter que se alistar um dia...')
    print('falta {} ano(s)'.format(18 -(date.today().year - nasc)))
elif date.today().year - nasc == 18:
    print('ALISTE jÁ! VOCÊ VAI PODER PULAR DE PARAQUEDAS, DAR TIRO DE CANHAO')
else:
    print('Já passou o tempo de se alistar!')
    print('Passou {} ano(s)'.format((date.today().year - nasc) - 18))
