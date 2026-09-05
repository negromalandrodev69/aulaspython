print("Olá sou uma calculadora de valores")
print("Quanto custou sua compra?: ")
valor_original = float(input())
print("o valor original era: R$", valor_original)
valor_economizado = valor_original / 100 * 15
print("Tu economizou : R$", valor_economizado)
valor_total = valor_original - valor_economizado
print("O valor que tu gastou foi: R$", valor_total)