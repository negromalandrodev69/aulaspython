from Animal import Animal

class Ave(Animal):
    def __init__(self, nome, idade, fome):
        super().__init__(nome="Sky", idade=2, nivel_fome=75, envergadura_asas=120)

    def voar(self, fome):
        if fome < 80:
            print("")

