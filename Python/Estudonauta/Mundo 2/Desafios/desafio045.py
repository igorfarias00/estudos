import random
jogador = input('Digite sua jogada(Tesoura | Pedra | Papel ): ').lower()

opcao = ["tesoura", "pedra", "papel"]

maquina = random.choice(opcao)

if jogador == maquina:
    print('Empate')
elif jogador == "tesoura" and maquina == "pedra" or jogador == "papel" and maquina == "tesoura":
    print("Maquina ganhou")
else:
    print("Jogador ganhou!!")

print(maquina)

