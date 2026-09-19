class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade_estoque = quantidade_estoque

    def adicionar_q(self, adicionar_qq, quantidade_estoque):
        if adicionar_qq <= 0:
            print("Erro: Quantidade inválida")
        else:
            self.__quantidade_estoque += 1
    def adicionar_v(self, vendas, quantidade_estoque):
        if vendas > self.__quantidade_estoque:
            print("Venda negada: Estoque insuficiente")
        else:
            self.__quantidade_estoque -= 1
    def adicionar_ad(self,desconto, preco):
        if desconto < 0 > 80% preco:
            print("Erro: Desconto inválido")
        else:
            self.__preco - desconto
    def resumo(self,nome,preco,quantidade_estoque):
        print(self.__nome,self.__preco,self.__quantidade_estoque)

 # 1. Tente forçar a alteração direta dos atributos (O Python permite criar variável fora, mas não altera a original):
 # meu_produto.__quantidade_estoque = -50
 # meu_produto.__preco = -100

 # 2. Tente realizar uma venda absurdamente maior do que o estoque que você cadastrou inicialmente:
 # meu_produto.realizar_venda(9999)

 # 3. Exiba o resumo final. O estoque e o preço reais não podem ter sido afetados pelos testes maliciosos acima!
 # meu_produto.exibir_resumo()





