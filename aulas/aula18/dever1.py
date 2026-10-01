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
