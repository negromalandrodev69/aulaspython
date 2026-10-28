# Leia todos os dados do arquivo dados_despadronizados.csv  e faça a formatação para aceitar todos os CPFs, números e salários.
#
# Depois dos dados validados, escreva um novo documento dados_padronizados.csv com os valores das colunas formatadas, e também delas validadas(booleano).
#
# COLUNAS DESEJADAS: nome, cpf, cpf_formatado, cpf_valido, numero, numero_formatado, numero_valido, salario, salario_formatado
#
# Utilize os metotos feitos em sala de aula para formatar os dados usando o .str e .replace.

import pandas as pd

funcionarion0 = pd.DataFrame([
        {
        'nome': "Renatão",
        'cpf': "123.456.789-04",
        'numero': "00 00 00000-0000",
        'salario': "5.0000"
        },
        {
        'nome': "Carlinhos",
        'cpf': "66000353780",
        'numero': "3434343434444",
        'salario': "R$10,000"
        },
        {
        'nome': "Jones",
        'cpf': "0-0-0-07769600",
        'numero': "+55 (21) 99876-5432",
        'salario': "14.00,050"
        }
    ])

dados = pd.read_csv("dados_despadronizados.csv",
                    dtype= {"cpf": str,"salario": str,"numero": str}, sep = ",")


cpf_f = (dados["cpf"].str.replace(r"\D","",regex = True))
# dados.insert(2, "cpf_formatado", dados["cpf"].str.replace(r"\D", "", regex=True))
salario_f = (dados["salario"]
                    .str.replace(r"[^\d,.\-]", "", regex=True)
                    .str.replace(r"\.(?=\d{3}(?:\.|,|$))", "", regex=True)
                    .str.replace(r",",".", regex=False))
salario_f = pd.to_numeric(salario_f, errors="coerce")
numero_f = (dados["numero"]
                    .str.replace(r"\D" , "", regex=True)
                    .str.replace(r",",".", regex=False))

dados_puros = dados[["nome","cpf","numero","salario"]]

dados.insert(2,"cpf_form",cpf_f)
dados.insert(4,"numero_form",numero_f)
dados.insert(6,"salario_form",salario_f)

print(dados.columns.tolist())
print(dados.to_string())

dados.to_csv("dados_padronizados.csv", index=False, sep=";")