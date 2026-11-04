import pandas as pd

estoque_supermercado = pd.read_csv("estoque_supermercado.csv",dtype= {"cpf": str,"salario": str,"numero": str}, sep = ",")

print(estoque_supermercado)

preco_corrigido = (estoque_supermercado["preco"]
                                                .str.replace(r"\D","",regex = True))
preco_corrigido = pd.to_numeric(preco_corrigido, errors="coerce")

quantidade_corrigida = (estoque_supermercado["quantidade"].str.replace(r"\D","",regex = True)
                                                          .str.replace(r"","sem setor",regex = True))

setor_corrigido = (estoque_supermercado["setor"].str.replace(r" ","",regex = True)
                     )

estoque_supermercado.insert(2,"PrecoV",preco_corrigido)
estoque_supermercado.insert(4,"QuantidadeV",quantidade_corrigida)

print(estoque_supermercado.columns.tolist())
print(estoque_supermercado.to_string())


# salario_f = (dados["salario"]
#                     .str.replace(r"[^\d,.\-]", "", regex=True)
#                     .str.replace(r"\.(?=\d{3}(?:\.|,|$))", "", regex=True)
#                     .str.replace(r",",".", regex=False))
# salario_f = pd.to_numeric(salario_f, errors="coerce")