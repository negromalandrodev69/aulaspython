#Crie uma única função que receba como parâmetro o nome de um aluno, sua nota do primeiro, segundo, terceiro e quarto bimestre.
#Sua função deve calcular a média final desse aluno, e imprimir na tela todos os valores, e informar se o aluno foi reprovado ou aprovado pela média final.
#OBS: valor da media = 7
#usar "def"
def media():
    nome = str(input("Coloque o nome do aluno: "))
    nota1 = float(input("Digite a nota do primeiro semestre: "))
    nota2 = float(input("Digite a nota do segundo semestre: "))
    nota3 = float(input("Digite a nota do terceiro semestre: "))
    nota4 = float(input("Digite a nota do quarto semestre: "))
    nota_final = nota1 + nota2 + nota3 + nota4 / 2
    return nome, nota_final
print(media())