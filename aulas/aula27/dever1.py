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