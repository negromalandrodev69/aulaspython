numero = int(input("digite numeros aleatoriamente: "))
numero_soma = 0
while numero != 0:
    numero_soma += numero
    numero = int(input("digite mais numeros aleatoriamente: "))
    if numero == 0:
        print("A soma dos numeros é ", numero_soma)
        break