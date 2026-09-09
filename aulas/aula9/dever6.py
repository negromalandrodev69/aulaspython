# Jogo de adivinhação

numero_secreto = 100

numero_digitado = int(input("Tente adivinhe o numero secreto: "))

while numero_secreto != numero_digitado:
    print("Você errou, tente novamente")
    numero_digitado = int(input("Tente adivinhe o numero secreto: "))

    print(f"Você ganhou, a senha era {numero_secreto}")

    opcao = input("Quer que o progama finalize? (sim) (não)")
    if opcao == "sim":
        break