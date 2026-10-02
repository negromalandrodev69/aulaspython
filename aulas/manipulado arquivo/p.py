produtos = []

produtos.append("Leite")
produtos.append("Macarrao")
produtos.append("Carne")
produtos.append("Açaí")
produtos.append("Iogurte")

for produto in produtos:
    print(produto)

# ESCRITA -> Write -> 'r'
# open -> Cria/Use 'arquivo.txt'
# as -> cria variável arquivo, e atribui o valores do documento
# arquivo.txt à ela
# with open("recibo.txt", 'w', encoding='utf-8') as arquivo:
#      for produto in produto
#          arquio.write(f"{produto}\n")

with open("recibo.txt", 'w', encoding='utf-8') as arquivo:
    for produto in produtos:
        arquivo.write(f"{produto}\n")

# LEITURA -> read -> 'r'
# open -> ler todos os texto escritos dentro do recibo.txt
with open("recibo.txt", 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()

    posicao = texto.find("Açaí")

    print(posicao)

    produto_vencido = texto[posicao:posicao+4]
    print(f"O produto {produto_vencido} está vencido.")