valor = float(input('Digite o valor do produto: R$'))
opcao = int(input('''Digite uma opcao: 
1 - à Vista dinheiro | cheque: 10% de desconto
2 - à Vista no cartão: 5% de desconto
3 - em até 2x no cartão: preço normal
4 - em até 3x mp cartão: 20% de juros  
'''))
acrescimo = 0
desconto = 0
if opcao == 1:
    desconto = valor * 0.10
elif opcao == 2:
    desconto = valor * 0.05
elif opcao == 3:
    desconto = 0
elif opcao == 4:
    acrescimo = valor * 0.20

valorFinal = (valor - desconto) + acrescimo
print('O preco final é {}'.format(valorFinal))