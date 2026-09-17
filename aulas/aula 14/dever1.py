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

    def MostrarAlmaP(self):
        print(self.nome, self.idade, self.cor, self.cheiro, self.relacao)

    def __str__(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}\nCheiro: {self.cheiro}\nRelação: {self.relacao}\n"


pessoa1 = P1(
    nome="JOAO",
    idade="22",
    cor="PRETO",
    cheiro="AÇO",
    relacao="PLATONICA"
)