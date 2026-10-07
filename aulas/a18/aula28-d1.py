with open("texto", 'r') as file:
    leitura = file.readline()
    cl = []
    for linha in leitura:
        print(leitura.strip())