print("Qualto tu gastou hoje?")
gasto = int(input())
print("Tu é um cliente VIP? 1 = sim, 0 = não")
Vip = int(input())
print("Você recebeu frete?", gasto >= 199 and Vip == 1)

