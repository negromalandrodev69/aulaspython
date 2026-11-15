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
#minha solução
#leitura["Lucromax"] = (leitura["Preco_Unitario"] * leitura["Quantidade"])
#Lucromaxes = (leitura.groupby("Mercado")["Lucromax"].sum())
#solução do claude
#5
preco = leitura["Preco_Unitario"].to_numpy()
qtd = leitura["Quantidade"].to_numpy()

faturamento = preco * qtd                      # array com o faturamento de cada venda
leitura["Faturamento"] = faturamento

total_rede = np.sum(faturamento)
print(f"Faturamento total da rede: R$ {total_rede:.2f}")

# faturamento por mercado
mercados = leitura["Mercado"].unique()
fat_mercado = np.array([
    faturamento[leitura["Mercado"].to_numpy() == m].sum() for m in mercados
])

i = np.argmax(fat_mercado)                     # posição do maior valor
print(f"\nMercado com maior receita: {mercados[i]} (R$ {fat_mercado[i]:.2f})")

print(Lucromaxes)

#6 ainda não tentei

#6
leitura["Preco_Promo"] = np.where(
    leitura["Quantidade"] >= 10,               # condição
    leitura["Preco_Unitario"] * 0.90,          # se verdadeiro: 10% de desconto
    leitura["Preco_Unitario"]                  # se falso: preço normal
)

leitura["Faturamento_Promo"] = leitura["Preco_Promo"] * leitura["Quantidade"]

novo_total = leitura["Faturamento_Promo"].sum()
print(f"Novo faturamento total da rede: R$ {novo_total:.2f}")
