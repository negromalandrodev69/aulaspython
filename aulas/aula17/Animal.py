class Animal():
    def __init__(self, nome, idade, fome):
        self.__nome = nome
        self.__idade = idade
        self.__fome = fome
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    @property
    def idade(self):
        return self.__idade
    @idade.setter
    def idade(self, idade):
        self.__idade = idade
        if idade < 0:
            print("ERRO: idade invalida")
    @property
    def fome(self):
        return self.__fome
    @fome.setter
    def fome(self, fome):
        self.__fome = fome
        if fome < 0:
            self.__fome = 0
        if fome > 100:
            self.__fome = 100

    @property
    def alimentar(self,porcao):
        if porcao <= 0:
            print("ERRO: porção invalida")
        else:
            self.__fome = porcao

    @property
    def emitir_s(self):
        print(f"{self.__nome}faz som genérico")

    @property
    def resumo(self):
        return f"O {self.__nome} tem {self.__idade} anos e está com {self.__fome} nivel de fome"
