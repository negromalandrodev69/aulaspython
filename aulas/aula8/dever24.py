print("Me informe um numero")
numero1 = int(input())
print("Agora me informe outro")
numero2 = int(input())
print("Agora me fale uma operação matemática entre (+) (-) (*) (/) ")
numero3 = str(input())
numerom = numero1 + numero2
numeron = numero1 - numero2
numerox = numero1 * numero2
numerop = numero1 / numero2
match numero3 :
    case "+":
        print(numerom)
    case "-":
        print(numeron)
    case "*":
        print(numerox)
    case "/":
        print(numerop)
    case _ :
        print("Numero invalido")