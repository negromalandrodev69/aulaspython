import json

loja = {
    'nomeT': 'Techstore',
    'produtos':
        [
            {
                "nome": "fone",
                "preco": 200,
                "estoque": 100
            },
            {
                "nome": "mouse",
                "preco": 45,
                "estoque": 60
            }
        ]
    }

with open ("recibo.json", 'w', encoding="utf-8") as file:
    json.dump(loja, file,indent=4 , ensure_ascii=False)

with open ("recibo.json", 'r', encoding="utf-8") as file:
    dados_lidos = json.load(file)
    for produto in dados_lidos.values["produtos"]:
        print(f"Produto: {produto['nome']} Preços: {produto['preco']}")