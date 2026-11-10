import pandas as pd

estoque_supermercado = pd.read_csv("estoque_supermercado.csv", dtype= {"cpf": str, "salario": str, "numero": str}, sep =",")

print(estoque_supermercado)

preco_corrigido = (estoque_supermercado["preco"].str.replace(r"\D","",regex = True))
preco_corrigido = pd.to_numeric(preco_corrigido, errors="coerce")

quantidade_corrigida = (estoque_supermercado["quantidade"].str.replace(r"","sem setor",regex = True))

setor_corrigido = (estoque_supermercado["setor"].str.replace(r" ","",regex = True))

estoque_supermercado.insert(2,"PrecoV",preco_corrigido)
estoque_supermercado.insert(4,"QuantidadeV",quantidade_corrigida)
estoque_supermercado.insert(6,"SetorV",setor_corrigido)

print("\n--- BASE DE DADOS LIMPA ---")
print(estoque_supermercado.columns.tolist())
print(estoque_supermercado.to_string())
print("\n--- PRODUTOS VENCENDO ESTA SEMANA ---")
# colocar valores já filtrados
print("\n--- MAIOR QUANTIDADE A VENCER ---")
# repetir o processo

#COMENTARIOS

#Possivel solução
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