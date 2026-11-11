import pandas as pd
import numpy as np

estoque_supermercado = pd.read_csv("estoque_supermercado.csv", sep =",")

preco_corrigido = (estoque_supermercado["preco"].str.replace(r"\D","",regex = True))
preco_corrigido = pd.to_numeric(preco_corrigido, errors="coerce")
preco_corrigido = preco_corrigido.fillna(preco_corrigido.mean()).round(2)

estoque_supermercado["valor_total_estoque"] = estoque_supermercado["quantidade"] * preco_corrigido["preco"]

quantidade_corrigida = (
    estoque_supermercado["quantidade"]
    .str.replace(r"\D","",regex = True)
)
quantidade_corrigida = pd.to_numeric(quantidade_corrigida, errors="coerce")
quantidade_corrigida = quantidade_corrigida.fillna(0)

setor_corrigido = (estoque_supermercado["setor"].str.replace(r" ","",regex = True))

estoque_supermercado.insert(2,"PrecoV",preco_corrigido)
estoque_supermercado.insert(4,"QuantidadeV",quantidade_corrigida)
estoque_supermercado.insert(6,"SetorV",setor_corrigido)

dataV = pd.to_datetime(estoque_supermercado["data_compra"], format="%d/%m/%Y", errors="coerce")
vencimentoV = pd.to_datetime(estoque_supermercado["data_vencimento"], format="%d/%m/%Y", errors="coerce")

hoje = pd.Timestamp("27-10-2026")
hoje_s = pd.Timestamp("03-11-2026")

print("\n--- BASE DE DADOS LIMPA ---")
print(estoque_supermercado.to_string())
print("\n--- PRODUTOS VENCENDO ESTA SEMANA ---")
dataV2 = estoque_supermercado[(vencimentoV >= hoje) & (vencimentoV <= hoje_s)]
print(dataV2)
print("\n--- MAIOR QUANTIDADE A VENCER ---")
if not dataV2.empty:
    print(dataV2.loc[dataV2["quantidade"].idxmax()])
else:
    print("Nenhum produto vence essa semana")
print("\n--- COMPRAS RECENTES (ÚLTIMOS 3 DIAS) ---")
cr = estoque_supermercado[
    (dataV >= 24-10-2026) & (dataV <= hoje)
]
print("\n--- PRODUTOS SEM DATA DE VENCIMENTO ---")
print(estoque_supermercado[estoque_supermercado["data_vencimento"].isna()])

print("\n--- MAIOR VALOR PATRIMONIAL POR SETOR ---")
por_setor = estoque_supermercado.groupby("Setor")["valor_total_estoque"].sum().sort_values(ascending=False)
print(f"\nSetor com maior valor parado: {por_setor.idxmax()} (R$ {por_setor.max():.2f})")
#COMENTARIOS

#Possivel solução
#
# preco_corrigido = (estoque_supermercado["preco"].astype(str)
#                                                 .str.replace("R$", "", regex=False)
#                                                 .str.strip
#                                                 .str.replace(",", ".", regex=False)
#
# setor_corrigido = (estoque_supermercado["setor"].str.replace(r" ","",regex = True)
#                                                 .str.strip()
#                                                 .str.lower() # Ver o que faz
#                                                 .str.replace(r" ",np.nan) # Ver o que o np.nan
#                                                 .fillna("sem setor") # Ver o que fillna faz
#
# dataCF = pd.to_datetime(estoque_supermercado["data_compra"], format="%d/%m/%Y", errors="coerce") # Não sei como usar isso
# dataVF = pd.to_datetime(estoque_supermercado["data_vencimento"], format="%d/%m/%Y", errors="coerce")
#
# hoje = pd.Timestamp("2026-10-27") # Não sei usar isso
#
#orientação
# salario_f = (dados["salario"]
#                     .str.replace(r"[^\d,.\-]", "", regex=True)
#                     .str.replace(r"\.(?=\d{3}(?:\.|,|$))", "", regex=True)
#                     .str.replace(r",",".", regex=False))
# salario_f = pd.to_numeric(salario_f, errors="coerce")

