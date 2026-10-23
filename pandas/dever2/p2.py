# Leia os dados do arquivo funcionarios.csv e crie um novo arquivo chamado cargos_altos.csv, contendo apenas os funcionários com salário acima de 6000 X
# Cadastre mais funcionários, cada um com id, nome, salario e cargo, utilizando cargos diferentes dos já existentes X
# Remova os dois primeiros funcionários do arquivo, considerando os índices (index) 0 e 1 X
# Crie uma nova coluna chamada tempo_empresa, que armazenará o tempo de permanência de cada funcionário na empresa em meses, utilizando valores do tipo inteiro (int) X
# Adicione um novo funcionário com o cargo de Estagiário, registrando seu tempo de empresa como int.
# Confira se as alterações foram aplicadas corretamente e se os arquivos CSV estão salvos com os dados atualizados.

import pandas as pd

sepa = pd.read_csv('../dever1/funcionarios.csv',
                   sep = ";")
funcionarion0 = [
        {
        'identificador': 31,
        'funcionario': 'Magnus Carlsen',
        'salario': 400,
        'cargo': "Jovem Aprendiz"
        },
        {
        'identificador': 32,
        'funcionario': 'ET',
        'salario': 2100,
        'cargo': 'Zelador'
        },
        {
        'identificador': 33,
        'funcionario': 'Simas',
        'salario': 3405,
        'cargo': 'Cozinheiro'
        }
    ]


sa = sepa[
    (sepa['salario'] > 6000)
]

funcionarion0 = pd.DataFrame(funcionarion0)
sepa = pd.DataFrame(sepa)
sa = pd.DataFrame(sa)

SAdataframe = pd.concat([sa,funcionarion0], ignore_index=True)

SAdataframe.to_csv("cargos_altos.csv", index=False, sep = ";")

SAdataframe = SAdataframe.drop(index=0)
SAdataframe = SAdataframe.drop(index=1)

SAdataframe['TempoMensal'] = [7,4,8,5,2,4]

novoF = [
    {
        'identificador': 34,
        'funcionario': 'Daniel',
        'salario': 50,
        'cargo': 'Estagiário',
        'TempoMensal': 1
    }
]

# novoF = pd.DataFrame(novoF)

# SAdataframe = pd.concat([sa,funcionarion0,novoF], ignore_index=True)

print(SAdataframe)