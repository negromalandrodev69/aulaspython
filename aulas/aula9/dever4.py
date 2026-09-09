numero = 0
print("1 - Mostrar saudação 2 - Sair do programa")
while numero == 1 or 2:
    numero = int(input("Escolha um: "))
    if numero == 1:
        print("Olá, seja muito bem-vindo(a)!")
    if numero == 2:
        print("Programa encerrado!")
        break
    if numero > 2 or numero < 1:
        print("Valor invalido!")