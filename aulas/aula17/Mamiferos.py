from Animal import Animal

class Mamifero(Animal):

    def __init__(self):
        super().__init__(nome = "Leão", idade = 2, fome = 70)
        self.__correr_kmh = 80

    def correr(self):
        if self.__correr_kmh > 0:
            print(f"{self.nome} correu a {self.__correr_kmh} km/h")
            return

    def emitir_s(self):
        print(f"{self.nome} faz som genérico")

obj = Mamifero()
print(obj.resumo)
obj.emitir_s()

