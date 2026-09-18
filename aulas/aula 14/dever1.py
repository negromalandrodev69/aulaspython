#Crie uma classe que tenha no mínimo 5 atributos, 1 construtor, 3 métodos convencionais.
#Sua classe deve ser uma das opções abaixo:
    #Carro
    #Banco
    #Pessoa
#Você escolhe quais atributos relacionar com o conceito da sua classe.
#No final, quero 5 objetos diferentes instanciados, e seu programa deve exibir em uma lista FORA da classe todos os seus objetos.

class Pessoa:
    def __init__(self, nome, idade, cor, cheiro, relacao):
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.cheiro = cheiro
        self.relacao = relacao

    def mostrarN(self):
        print(self.nome)
    def mostrarI(self):
        print(self.idade)
    def mostrarIC(self):
        print(self.cor)
    def mostrarC(self):
        print(self.cheiro)
    def mostrarR(self):
        print(self.relacao)

    def __str__(self):
         return f"Nome: {self.nome}\nIdade: {self.idade}\nCor: {self.cor}\nCheiro: {self.cheiro}\nRelação: {self.relacao}\n"


pessoa1 = Pessoa("Camila", 28, "Branca", "Amendoa", "Amizade")
pessoa2 = Pessoa("Carlos", 34, "Preto", "Ferro", "Empresarial")
pessoa3 = Pessoa("Elena",42,"Parda", "Vinho Tinto", "Maternal")
pessoa4 = Pessoa("Renan", 33 , "Branco", "Academia", "Parasocial")
pessoa5 = Pessoa("Victor",27 , "Avermelhado", "Baunilha", "Romântica")

TodasP = [pessoa1, pessoa2, pessoa3, pessoa4, pessoa5]
print(TodasP)
for Pessoa in TodasP:
    print(Pessoa.nome)

escolha = input("Qual dessas pessoas você quer saber as propriedades?")
if escolha == "1":
    print(Pessoa.mostrarN(), Pessoa.mostrarI(), Pessoa.mostrarIC(), Pessoa.mostrarC(), Pessoa.mostrarR())
if escolha == "2":
    print(Pessoa.mostrarN(), Pessoa.mostrarI(), Pessoa.mostrarIC(), Pessoa.mostrarC(), Pessoa.mostrarR())
if escolha == "3":
    print(Pessoa.mostrarN(), Pessoa.mostrarI(), Pessoa.mostrarIC(), Pessoa.mostrarC(), Pessoa.mostrarR())
if escolha == "4":
    print(Pessoa.mostrarN(), Pessoa.mostrarI(), Pessoa.mostrarIC(), Pessoa.mostrarC(), Pessoa.mostrarR())
if escolha == "5":
    print(Pessoa.mostrarN(), Pessoa.mostrarI(), Pessoa.mostrarIC(), Pessoa.mostrarC(), Pessoa.mostrarR())