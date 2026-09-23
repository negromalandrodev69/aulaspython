class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade_estoque = quantidade_estoque

    def adicionar_q(self,quantidade_estoque, quantidade):
        if quantidade <= 0:
            print("Erro: Quantidade inválida")

        else:
            self.__quantidade_estoque += quantidade
    def adicionar_v(self, quantidade):
        if quantidade <= 0 or quantidade > self.__quantidade_estoque:
            print("Venda negada: Estoque insuficiente")
        else:
            self.__quantidade_estoque -= quantidade
    def adicionar_ad(self,percentual):
        if percentual <= 0 or percentual > 80:
            print("Erro: Desconto inválido")
        else:
            self.__preco = self.__preco * (1 - percentual / 100)
    def resumo(self):
        print(f"Produto : {self.__nome} Preço : {self.__preco} Estoque: {self.__quantidade_estoque}")

meu_produto = Produto(nome="Teclado", preco=70, quantidade_estoque=30)

meu_produto.__quantidade_estoque = -50
meu_produto.__preco = -100
meu_produto.adicionar_v(9999)
meu_produto.resumo()

 # 1. Tente forçar a alteração direta dos atributos (O Python permite criar variável fora, mas não altera a original):
 # meu_produto.__quantidade_estoque = -50
 # meu_produto.__preco = -100

 # 2. Tente realizar uma venda absurdamente maior do que o estoque que você cadastrou inicialmente:
 # meu_produto.realizar_venda(9999)

 # 3. Exiba o resumo final. O estoque e o preço reais não podem ter sido afetados pelos testes maliciosos acima!
 # meu_produto.exibir_resumo()





