orçamento = 500
gasto = 0
while orçamento > 0:
    gasto = float(input("Quanto você gastou ?"))
    orçamento_n = orçamento - gasto
    print("Você ficou com: ", orçamento_n)
    if orçamento < 0:
        print("Você ficou sem dinheiro")
        break