import json

lista_aniversariantes = []

with open("base1.json", 'r') as file:  # Feito para ler o json da forma correta
    dados1 = json.load(file)

with open("base2.json", 'r') as file:
    dados2 = json.load(file)

with open("base3.json", 'r') as file:
    dados3 = json.load(file)

for aniversariante in dados1:         # Adiciona o dicionario a uma lista global otimizando a leitura dela
    dicionario_aniversariante = {
        "nome": aniversariante['nome'],
        "aniversario": aniversariante['aniversario']
    }
    lista_aniversariantes.append(dicionario_aniversariante)

for aniversariante in dados2:
    dicionario_aniversariante = {
        "nome": aniversariante['nome'],
        "aniversario": aniversariante['aniversario']
    }
    lista_aniversariantes.append(dicionario_aniversariante)

for aniversariante in dados3:
    dicionario_aniversariante = {
        "nome": aniversariante['nome'],
        "aniversario": aniversariante['aniversario']
    }
    lista_aniversariantes.append(dicionario_aniversariante)
with open("aniversariantes.json", 'w') as arquivo:  # Escreve todos os valores de uma vez só
    json.dump(lista_aniversariantes, arquivo, indent=4, ensure_ascii=False)


with open("aniversariantes.json", 'r', encoding="utf-8") as file:
    leituraJ = json.load(file)
    for leitura in leituraJ:
        print(f"Nome: {leitura['nome']}| Aniversario: {leitura['aniversario']}")