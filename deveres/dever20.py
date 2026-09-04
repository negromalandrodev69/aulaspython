print("Qual produto queres? (1) (2) (3) (4)")
comida = int(input())
match comida:
    case 1:
        print("Cachorro-quente R$ 10,00.")
    case 2:
        print("Hamnbúrger R$ 15,00.")
    case 3:
        print("Batata Frita R$ 8,00.")
    case 4:
        print("Refrigerante R$ 5,00.")
    case _:
        print("numero invalido")