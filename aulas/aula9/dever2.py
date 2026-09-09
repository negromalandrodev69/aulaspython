senha = 123456
input("Digite sua senha: ")
while senha:
    print("Senha incorreta. Tente novamente.")
    senha = int(input())
    if senha == 123456:
        print("Acesso permitido")
        break