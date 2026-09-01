print("Olá sou uma calculadora de valores")
print("Quanto custou sua compra?: ")
valor_original = int(input())
print("o valor original era", valor_original)
valor_economizado = 15 % valor_original
print("Tu economizou", valor_economizado)
valor_total = valor_original - valor_economizado
print("O valor que tu gastou foi", valor_total)