import json

lista_aniversariantes = []
with open("base1.json", 'r',encoding="utf-8") as file: #Erro de repetição mal executada
    filtro_l = file.readlines()

    for leitura in filtro_l:
        base1 = leitura.strip().split(';')

        lista_aniversariantes.append(
                {
                    "Nome do(a): ": (base1[0]),
                    "Data do aniversario: ": (base1[1]),
                }
            )

with open("base2.json", 'r',encoding="utf-8") as file:
    filtro_l2 = file.readlines()

    for leitura in filtro_l2:
        base2 = leitura.strip().split(';')
        lista_aniversariantes.append(
                {
                    "Nome do(a): ": (base2[3]),
                    "Data do aniversario: ": (base2[4]),
                }
            )

with open("base3.json", 'r', encoding="utf-8") as file:
    filtro_l3 = file.readlines()

    for leitura in filtro_l3:
        base3 = leitura.strip().split(';')
        lista_aniversariantes.append(
                {
                    "Nome do(a): ": (base3[0]),
                    "Data do aniversario: ": (base3[3]),
                }
            )

with open ("ann.json", 'w', encoding="utf-8") as file:                  #repetições ineficazes
    json.dump(lista_aniversariantes, file,indent=4 , ensure_ascii=False)

with open ("ann.json", 'w', encoding="utf-8") as file:
    json.dump(lista_aniversariantes, file,indent=4 , ensure_ascii=False)

with open ("ann.json", 'w', encoding="utf-8") as file:
    json.dump(lista_aniversariantes, file,indent=4 , ensure_ascii=False)