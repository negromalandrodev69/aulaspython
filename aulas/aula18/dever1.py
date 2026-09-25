from abc import ABC, abstractmethod

class SistemaN(ABC):
    @abstractmethod
    def enviar(self,email, sms, pushnotification):
        pass

    def iniciar_processo(self):
        print ("O processo de verificação começou")
        return

class SMS(SistemaN):
    def verificar(self,sms):
        if sms > ["","","","","","","","",""]:
            return True
        else:
            return False
class Email2(SistemaN):
    def mail(self,email,sms):
        if sms == True:
            email = True
            return f"Numero validado seu email : {email} será enviado"
        else :
            email = False
            print ("Numero invalido seu :", email  ,"não será enviado")
            return False

def processar_lote(lista_de_objetos):

# 1. Tentativa de instanciar a Classe Abstrata (DEVE GERAR ERRO)
# Descomente a linha abaixo para testar e provar que o Python bloqueia:
# objeto_generico = SuaClassePai()

# 2. Instanciando as Classes Filhas
#     obj1 = ClasseFilha1()
#     obj2 = ClasseFilha2()

# 3. Criando um Lote de Processamento (Lista)
    #lote = [obj1, obj2, obj1]  # Pode repetir tipos

# 4. Processando em lote (Demonstrando o Polimorfismo e a Abstração)
#     print("\n--- INICIANDO PROCESSAMENTO EM LOTE ---")
#     for item in lote:
#         item.método
#         concreto
#         log()
#         # Chama o método que era abstrato, mas agora está implementado
#         item.metodo_abstrato(argumento1, argumento2)