import pandas as pd
import numpy as np

leitura = pd.read_csv("vendas_mercados.csv", dtype={"Cliente" : str,"Mercado" : str,"Regiao" : str,"Produto" : str,"Forma_Pagamento": str},sep =",")
#1
# leitura["Lucro_g"] = ((leitura["Preco_Unitario"] - leitura["Custo_Unitario"]) * leitura["Quantidade"])
#
# lucrom = (leitura.groupby("Mercado")["Lucro_g"].sum())
#
# regiao_m = lucrom.max()
# regiao_mn = lucrom.idxmax() # idxmax pega o maior fator por id

# print(lucrom)
# print(f"\nO mercado mais lucrativo foi {regiao_mn}, e teve o lucro de : R${regiao_m}\n")
#
# regs = leitura.groupby("Mercado").size()
# print(regs)

#2
# pixbet = leitura.groupby(["Regiao","Forma_Pagamento"])["ID_Venda"].size()
# print(pixbet)

#3
# maisv = leitura.groupby(["Produto"]).size()
# print(maisv)

#4
# lucromM = (leitura.groupby("Mercado")["Lucro_g"]).mean()
# print(lucromM)

#5
leitura["Lucromax"] = (leitura["Preco_Unitario"] * leitura["Quantidade"])
Lucromaxes = (leitura.groupby("Mercado")["Lucromax"].sum())

print(Lucromaxes)
