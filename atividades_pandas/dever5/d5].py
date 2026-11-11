import pandas as pd
import numpy as np

leituram = pd.read_csv("vendas_mercados.csv", dtype={"ID_Venda" : str,"Cliente" : str,"Mercado" : str,"Regiao" : str,
                                     "Produto" : str,"Quantidade": str,"Forma_Pagamento": str},sep =",")
#
# leituram = pd.read_csv("vendas_mercados.csv", dtype={"ID_Venda" : str,"Cliente" : str,"Mercado" : str,"Regiao" : str,
#                                      "Produto" : str,"Quantidade": str,"Preco_Unitario": str,"Custo_Unitario": str,"Forma_Pagamento": str},sep =",")