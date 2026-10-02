nome = str(input("Insira seu nome :"))
produtos = []
preco = []
total = 0

while True:
    print("Digite 'fim' para finalizar")
    produto_nome = str(input("Insira o nome seu produto :"))
    if produto_nome == "fim":
        break
    produto_preco = float(input("Insira o preco seu produto :"))
    total += produto_preco
    produtos.append([produto_nome,produto_preco])

with open ("produtos.txt",'w', encoding="utf-8") as file:
    file.write("RECIBO DAS COMPRAS\n\n")

    for produto in produtos:

        file.write(f"Produto: {produto[0]} R$: {produto[1]}\n")

    file.write(f"Compra processada com sucesso! Valor cobrado: R${total}\n")

with open ("produtos.txt", 'r', encoding="utf-8") as file:
    texto = file.read()
    p = texto.find("Valor cobrado: R$")
    print(p)