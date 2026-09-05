idade = int(input("Qual sua idade?"))
vip = bool(input("Você é VIP? 1 = sim, 0 = não"))
organizado = bool(input("Você é um organizador do evento? 1 = sim, 0 = não"))
True == 1
if organizado == True or idade >= 18 and vip == True:
    print("Entrada Permitida! seja bem vindo")
else:
     print("Entrada NEGADA! seja bem vindo")