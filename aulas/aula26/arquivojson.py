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
    for produto in dados_lidos["produtos"]:
        print(f"Produto: {produto['nome']} | Preços: {produto['preco']}")

with open ("recibo.json", 'w', encoding="utf-8") as file:
    dados_lidos["produtos"].append(
        {
            "nome": "cadeira ergonomica",
            "preco": 3000.00,
            "estoque": 6
        }
    )
    json.dump(dados_lidos, file, ensure_ascii=False, indent=4)

print("PREÇOS ATUALIZADOS")
for produto in dados_lidos["produtos"]:
    print(f"O {produto['nome']} agora custa R$ {produto['preco']:.2f}"
          f"\n Quantidade estoque: {produto['estoque']}")