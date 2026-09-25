from abc import ABC, abstractmethod

class Produto(ABC):
    @abstractmethod
    def enviar(self,valor,destino,peso):
        pass

    def registrare(self,processo):
        print("Seu processo :", processo ,"foi iniciado")

class Caminhao(Produto):
    def preco(self,peso,destino):
        destino = 20
        adicional = destino * peso
        return adicional
    def enviar(self,valor,destino,peso):
        print(f"enviando pelo caminhão com o peso de {peso}")
    def conclusao(self,adicional, valor):
        final = valor + adicional
        print("O valor final do seu produto foi de : ", final)
class Drone(Produto):
    def medida(self,peso):
        if peso > 4:
            return f"Esse peso é muito alto para o drone carregar"
    def enviar(self,valor,destino,peso):
        print(f"enviando pelo drone com o peso de {peso}")
    def preco(self,peso,destino):
        destino = 50
        adicional = destino * peso
class Navio(Produto):
    def enviar(self,valor,destino,peso):


encomenda = Caminhao()

encomenda.enviar(15000, "DF",200)