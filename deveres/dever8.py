caixa = 12
print("Qual a quantidade de maçãs você colheu hoje?")
quanti_maças = int(input())

maças_sobraram = quanti_maças % 12

quantidade_caixas = quanti_maças // 12

print("foram usadas",quantidade_caixas, "caixas")
print("A quantidade de maçãs que sobrou foi:",maças_sobraram,"maças" )
