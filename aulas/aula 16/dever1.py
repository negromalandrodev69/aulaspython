class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade_estoque = quantidade_estoque

    def Adicionar_Q(self, quantidade_estoque):
        if self.__quantidade_estoque > 0:

    def Adicionar_V(self, vendas):
        if self.__quantidade_estoque > 0:

    def Adicionar_AD(self, quantidade_estoque ):


 # 1. Tente forçar a alteração direta dos atributos (O Python permite criar variável fora, mas não altera a original):
 # meu_produto.__quantidade_estoque = -50
 # meu_produto.__preco = -100

 # 2. Tente realizar uma venda absurdamente maior do que o estoque que você cadastrou inicialmente:
 # meu_produto.realizar_venda(9999)

 # 3. Exiba o resumo final. O estoque e o preço reais não podem ter sido afetados pelos testes maliciosos acima!
 # meu_produto.exibir_resumo()





