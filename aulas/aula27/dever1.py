import json

with open("banco_livros", 'r', encoding="utf-8") as file:
    leitura_l = file.readlines()
    catalogo = []
    for leitura in leitura_l:
        banco_livros = leitura.strip().split(';')

        catalogo.append(
            {
                "idd" : int(banco_livros[0]),
                "nome" : str(banco_livros[1]),
                "descricao" : str(banco_livros[2]),
                "preco" : float(banco_livros[3]),
                "quantidade" : int(banco_livros[4]),
            }
        )

with open ("livraria.json", 'w', encoding="utf-8") as file:
    json.dump(catalogo, file,indent=4 , ensure_ascii=False)

livron = [
    {
        "idd" : 31,
        "nome" : "A metamorfose",
        "descricao" : "Ultimo livro de Franz Kafta",
        "preco" : 45,
        "quantidade" : 20,
    },
{
        "idd" : 32,
        "nome" : "O príncipe",
        "descricao" : "Livro que encarna os conceitos de politica",
        "preco" : 45,
        "quantidade" : 40,
    },
    {
        "idd" : 33,
        "nome" : "Crítica a razão pura",
        "descricao" : "Kant disserta sobre o conhecimento humano entre Apriori e Posteriori",
        "preco" : 45,
        "quantidade" : 15,
    },
    {
        "idd" : 34,
        "nome" : "O anti-cristo",
        "descricao" : "Um dos livros mais pesados de Friederic Nitche",
        "preco" : 45,
        "quantidade" : 30,
    },
    {
        "idd" : 35,
        "nome" : "A academia de Platão",
        "descricao" : "Conceitos do inicio a filosofia",
        "preco" : 45,
        "quantidade" : 5,
    },
]

catalogo.extend(livron)

with open ("livraria.json", 'w', encoding="utf-8") as file:
    json.dump(catalogo, file,indent=4 , ensure_ascii=False)

with open("livraria.json", 'r', encoding="utf-8") as file:
    leitura_l = json.load(file)
    for leitura in leitura_l:
        print(f"ID: {leitura['idd']}| Nome: {leitura['nome']}| Descrição: {leitura['descricao']}| Quantidade: {leitura['quantidade']}")

    valor_total_loja = 0

    for livro in leitura_l:
        if livro["quantidade"] <= 15:
            print(f'Esse livro: {livro["nome"]} tem menos de 15 no estoque.')