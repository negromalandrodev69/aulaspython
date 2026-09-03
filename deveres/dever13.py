print("Qual o nome do produto?")
nome = str(input())
print("Quanto custa para comprar esse produto?")
custo = int(input())
print("qual o valor que ira vender o produto?")
venda = int(input())
lucro = custo - venda
print(nome, lucro, "O lucro foi bom?", lucro >= 19)