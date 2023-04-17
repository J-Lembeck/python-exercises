import random

while True:
    secret = random.randint(1, 9)
    tries = 0
    while True:
        entrada = input("Escolha um número entre 1 e 9 ('sair' para sair): ")
        if entrada.lower() == 'sair':
            break

        try:
            palpite = int(entrada)
        except ValueError:
            print("Inválido. Por favor, digite um número entre 1 e 9 ou 'sair'")
            continue

        tries += 1

        if palpite < secret:
            print("O número é maior.")
        elif palpite > secret:
            print("O número é menor.")
        else:
            print("Correto! O número é {} tries.".format(tries))
            break

    try_again = input("Jogar novamente? (S/N): ")
    if jogar_novamente.lower() != 's':
        break
