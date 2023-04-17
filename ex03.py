while True:
    player1 = input("Jogador 1, escolha entre pedra, papel e tesoura: ").lower()
    player2 = input("Jogador 2, escolha entre pedra, papel e tesoura: ").lower()

    if player1 not in ["pedra", "papel", "tesoura"] or player2 not in ["pedra", "papel", "tesoura"]:
        print("Inválida. Tente novamente.")
        continue

    if player1 == player2:
        print("Empatou!")
    elif (player1 == "pedra" and player2 == "tesoura") or (player1 == "tesoura" and player2 == "papel") or (player1 == "papel" and player2 == "pedra"):
        print("Jogador 1 ganhou!")
    else:
        print("Jogador 2 ganhou!")

    jogar_novamente = input("Jogar novamente? (S/N): ").lower()
    if jogar_novamente != "s":
        break

