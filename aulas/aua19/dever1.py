class ItemPedido:
    def __init__(self,descricao = str,valor = float):
        self.descricao = descricao
        self.valor = valor
        if valor == str:
            try :
                print("Erro: O valor para '[descricao]' deve ser estritamente numérico.")
            finally:
                self.valor = float

class Mesa:
    def __init__(self,item,taxa_serviço,lista_pedidos,numero_mesa):
        self.item = item
        self.taxa_servico = taxa_serviço
        self.lista_pedidos = lista_pedidos
        self.numero_mesa = mesa
    def adicionar_pedido(self,ItemPedido,numero_mesa):
        self.lista_pedidos.append(ItemPedido)

