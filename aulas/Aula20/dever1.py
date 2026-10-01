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

with open ("produtos.txt",'w') as file:
    for produto in produtos:
        file.write(produto[0]+"\n")
