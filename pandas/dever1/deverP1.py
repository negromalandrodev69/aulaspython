# todos os salários menores do que 3000, maiores do que 5000 mil e iguais a 3100
# todos os cargos de Analista de Dados, Analista de Sistemas, Desenvolvedor Java e Cientista de dados
# listar os nomes e cargos de quem tem um salário maior do que 6000
# listar todos os funcionarios com id par, para fazer = %2 = True
import csv

import pandas as pd

#1
func = pd.read_csv('funcionarios.csv',
                   sep = ";")

filtrex = func[
    (func['salario'] < 3000) |
    (func['salario'] > 5000) |
    (func['salario'] == 3100)
]

print("\n★FILTRO SALARIAL: \n")
print(filtrex)

#2
filtrocol = func[
    (func['cargo'] == 'Analista de Dados') |
    (func['cargo'] == 'Analista de Sistemas') |
    (func['cargo'] == 'Desenvolvedor Java') |
    (func['cargo'] == 'Cientista de Dados')
]
print("\n★FILTRO DE CARGOS: ★\n")
print(filtrocol)

#3
filtrexx = func[
    (func['salario'] > 6000)
]
print("\n★FILTRO SALARIAL ALTO: \n")
print(filtrexx)

#4
filtrid = func[
    (func['id'] % 2 == 0)
]
print("\n★FILTRO DE ID: \n")
print(filtrid)