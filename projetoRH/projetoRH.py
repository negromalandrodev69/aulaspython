import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1 Exploração inicial / leitura
rh = pd.read_csv("funcionariosrh.csv",dtype={"id_registro":str,"id_funcionario":str,"nome_funcionario":str,"idade":str,"sexo":str,
                                              "escolaridade":str,"departamento":str,"cargo":str,"nivel_hierarquico":str,"salario":str,"data_admissao":str,
                                              "data_desligamento":str,"data_referencia":str,"tipo_contrato":str,"modalidade_trabalho":str,
                                              "avaliacao_desempenho":str,"horas_treinamento":str,"quantidade_promocoes":str,"status_funcionario":str}
                                              ,encoding="UTF-8", sep = ";")
# print(rh.to_string()) # 49.999 registros
# contagem de funcionarios unicos
contar_func = rh.groupby(["id_registro","id_funcionario"])["nome_funcionario"].sum()
print(contar_func.to_string()) # talvez 8.335 funcionarios
# classifcar os tipos dos dados da lista
classificar_v =

# 2 Limpeza e qualidade
filtro_idade = rh["idade"].str.replace(r"\D",np.nan,regex=True)
filtro_idade = pd.to_numeric(filtro_idade,errors="coerce")
filtro_salario = rh["salario"].str.replace(r"\D",np.nan,regex=True)
filtro_salario = pd.to_numeric(filtro_salario,errors="coerce")
filtro_salario = rh["salario"].fillna("Valor invalido")
filtro_hierarquico = rh["nivel_hierarquico"].str.replace("\D",np.nan,regex=True)
filtro_hierarquico = pd.to_numeric(filtro_hierarquico,errors="coerce")
filtro_hierarquico = rh["nivel_hierarquico"].fillna("Valor invalido")
filtro_desempenho = rh["avaliacao_desempenho"].str.replace("\D",np.nan,regex=True)
filtro_desempenho = pd.to_numeric(filtro_desempenho,errors="coerce")
filtro_desempenho = rh["avalicao_desempenho"].fillna("Valor invalido")
filtro_treinamento = rh["horas_treinamento"].str.replace("\D",np.nan,regex=True)
filtro_treinamento = pd.to_numeric(filtro_treinamento,errors="coerce")
filtro_treinamento = rh["tipo_contrato"].fillna("Valor invalido")
filtro_promocoes = rh["quantidade_promocoes"].str.replace("\D",np.nan,regex=True)
filtro_promocoes = pd.to_numeric(filtro_promocoes,errors="coerce")
filtro_promocoes = rh["quantidade_promocoes"].fillna("Valor invalido")