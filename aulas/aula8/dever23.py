print("Em qual mês do ano estamos?")
mes = int(input())
match mes :
    case "12" | "1" | "2" :
        print("Estamos no Verâo")
    case "3" | "4" | "5" :
        print("Estamos no Outono")
    case "6" | "7" | "8" :
        print("Estamos no Inverno")
    case "9" | "10" | "11" :
        print("Estamos na Primavera")
    case _ :
        print("Mês inválido")