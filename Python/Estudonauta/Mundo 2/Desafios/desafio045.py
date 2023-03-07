import random
jogador = input('Digite sua jogada(Tesoura | Pedra | Papel ): ').lower()

opcao = ["tesoura", "pedra", "papel"]

maquina = random.choice(opcao)
if jogador in opcao:
    if jogador == maquina:
        print('Empate')
    elif jogador == "tesoura" and maquina == "pedra" or jogador == "papel" and maquina == "tesoura" or jogador == "pedra " and maquina == "papel":
        print("Maquina ganhou")
    else:
        print("Jogador ganhou!!")
else:
    print('Opcao invalida!!')

print(maquina)

