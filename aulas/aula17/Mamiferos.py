from Animal import Animal

class Mamifero(Animal):

    def __init__(self, nome, idade, fome):
        super().__init__(nome = "Leão", idade = 2, fome = 70, correr_kmh = 80)

    def correr(self,fome,correr_kmh):
        if correr_kmh > 0:
            fome - 20
            print(self.__nome, "correu a",{correr_kmh}, "km/h")
            return

    def emitir_r(self,nome):
        print (self.__nome,"Ruge alto")

    def resum2(self):
        print
