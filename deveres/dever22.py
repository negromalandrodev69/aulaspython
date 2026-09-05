print("Em qual turno tu estuda? M = matutino, V = vespertino, N = noturno")
turno = str(input())
match turno:
    case "M" | "m":
        print("Bom Dia!")
    case "V" | "v":
        print("Boa tarde!")
    case "N" | "n":
        print("Boa noite!")
    case _ :
        print("Turno inválido")