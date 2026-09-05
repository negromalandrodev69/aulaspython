saldo = float(input("Olá qual seu saldo atual?"))
saque = float(input("Quanto deseja sacar?"))
restante = saldo - saque

if saldo < saque:
    print("Saldo insuficiente")

elif saldo > saque:
    print("Saque realizado com sucesso!, saldo atual: ", restante)

