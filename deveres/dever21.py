print("Digite uma letra")
letra = str(input())
match letra:
    case "a" | "A" | "e" | "E" | "i" | "I" | "o" | "O" | "u" | "U":
        print("Você digitou uma vogal")
    case _:
        print("Não é uma vogal.")