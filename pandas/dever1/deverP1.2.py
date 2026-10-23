import pandas as pd

func = pd.read_cvd("funcionarios.csv",sep=";")
f = func.rename(columns={
    'id': "identificador",
    "nome": "funcionario"
})
print(func[['funcionario', 'identificador']])

funcionarion = [
    {
    'identificador': 31,
    'funcionario': 'Magnus Carlsen',
    'salario': 400,
    'cargo': "Jovem Aprendiz"
    }
]

func = func.concat([func, funcionarion], ignore_index=True)

print(func)