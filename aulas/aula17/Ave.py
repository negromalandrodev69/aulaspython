from Animal import Animal

class Ave(Animal):
    def __init__(self):
        super().__init__(nome="Sky", idade=2, fome=75)
        self.__envergadura_asas=120

    def voar(self, fome):
        if fome < 80:
            print ("Voo negado:", {self.nome},"está faminto demais para voar!")
        if fome >= 80:
            print(f"{self.nome} voou com suas asas de {self.__envergadura_asas} cm!")
            fome -= 15

    def emitir_s(self):
        print(f"{self.nome} canta um som melodioso!")



obj = Ave()
print(obj.resumo)
obj.emitir_s()