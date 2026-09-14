#Crie uma lista que ela armazene um numero x de funcionários. Usando o while, adicione quantos funcionários quiser em execução (input).
#Com o for, você irá imprimir duas listas:
#uma lista com todos os funcionários que receberão um aumento.
#Outra lista, com todos os funcionário que serão demitidos.
#Você irá decidir qual funcionário será demitido ou receberá aumento pelo index do funcionário lista[]

funcionarios = []
adicionar = ""
famuneto = []
aumento = []
demisao = []
almento = ""
demi = ""
while True:
    adicionar = str(input("Você quer adicionar um funcionario?(S/N): "))
    if adicionar == "N":
        break
    if adicionar == "S":
        funcionarios = str(input("Digite o nome do funcionario: "))
        print(funcionarios)
        aumento = str(input("você quer dar aumento a algum funionario?(S/N): "))
        if aumento == "N":
            break
        if aumento == "S":
            famuneto = str(input("Digite o nome do funcionario que recebera o aumento: "))
            if famuneto == funcionarios[0]:
                print("esse funcionario não existe")
