class ItemPedido:
    def __init__(self,descricao,valor):
        try:
            self.descricao = str(descricao)
        except ValueError:
            print("Descricao invalida,numeros não podem ser usados aqui")
        try:
            self.valor = float(valor)
        except ValueError:
            print("Valor invalido,use apenas numeros")
class Mesa:
    def __init__(self,numero_mesa):
        self.numero_mesa = int(numero_mesa)
        self.pedidos = []

    def adicionar_pedido(self,pedidos,numero_mesa):
        for pedido in pedidos:
            pedidos.append(pedido.descricao,pedido.valor)
            print(f"{pedido.descricao} adicionado a {numero_mesa}")
    def somar_total(self,total):
        total = 0
        for pedido in self.pedidos:
            total += pedido.valor
        return total

pedido1 = ItemPedido("Pizza",500)
mesa1 = Mesa(numero_mesa=1)
mesa1.adicionar_pedido(pedido1)