#Crie uma lista que ela armazene um numero x de funcionários. Usando o while, adicione quantos funcionários quiser em execução (input).
#Com o for, você irá imprimir duas listas:
#uma lista com todos os funcionários que receberão um aumento.
#Outra lista, com todos os funcionário que serão demitidos.
#Você irá decidir qual funcionário será demitido ou receberá aumento pelo index do funcionário lista[]

funcionarios = []
famuneto = []
demisao = []
while True:
    adicionar = str(input("Você quer adicionar um funcionario?(S/N): "))
    if adicionar == "N":
        break
    if adicionar == "S":
        funcionarios.append(str(input("Digite o nome do funcionario: ")))
while True:
    aumento = str(input("você quer dar aumento a algum funionario?(S/N): "))
    if aumento == "N":
        break
    if aumento == "S":
        famuneto.append(str(input("Digite o nome do funcionario que recebera o aumento: ")))
while True:
    demi = str(input("Você quer demitir algun funcionario?(S/N): "))
    if demi == "N":
        break
    if demi == "S":
        demisao.append(str(input("Digite o nome do funcionario: ")))

for famuneto in famuneto:
    print("Esses funcionarios: ", {famuneto}, ",receberão aumento")
for demisao in demisao:
    print("Já esses: ", {demisao}, ",receberão demisão")