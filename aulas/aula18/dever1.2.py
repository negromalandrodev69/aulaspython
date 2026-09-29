from abc import ABC, abstractmethod

class Produto(ABC):
    @abstractmethod
    def enviar(self,peso,valor,distancia):
        pass
    def iniciarP(self):
        print(f"O processo foi iniciado com sucesso!")

class Caminhao(Produto):
    def enviar(self,peso,valor,distancia):
        valor = distancia * 2
        print (f"Você ira pagar {valor} de frete")
        return

class Drone(Produto):
    def enviar(self,peso,valor,distancia):
        valor = distancia * 5
        if peso > 2:
            print("O peso é alto demais,opção drone indisponivel")
        else:
            print(f"O valor do frete será :{valor}")

obj1=Caminhao()
obj2=Drone()

processar_lote = []
processar_lote.append(obj1)
processar_lote.append(obj2)

# objeto_generico = Produto()
print("\n--- INICIANDO PROCESSAMENTO EM LOTE ---")

for produto in processar_lote:
    produto.enviar(peso=5, valor=3, distancia=10)
