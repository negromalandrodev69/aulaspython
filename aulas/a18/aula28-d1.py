def add_alunos():
    aluno_n = str(input("Digite o nome do aluno: "))
    turma = int(input("Digite a turma do aluno: "))
    not1 = float(input("Digite a 1 nota do aluno: "))
    not2 = float(input("Digite a 2 nota do aluno: "))
    not3 = float(input("Digite a 3 nota do aluno: "))
    not4 = float(input("Digite a 4 nota do aluno: "))
    media = (not1 + not2 + not3 + not4) / 4
    if media >= 7:
        estadop = "Aprovado"
    else :
        estadop = "Reprovado"

    with open('alunos.txt', 'a', encoding='utf-8') as file:
        file.write(f"{aluno_n};{turma};{not1};{not2};{not3};{not4};"
                      f"{estadop}\n")

def padronizartxt ():
    pesquisa = str(input("Digite o nome que quer saber a media: "))
    with open('alunos.txt', 'r', encoding='utf-8') as file:
        leitura = file.readlines()

        for alunos in leitura:
            alunos = alunos.strip()
            alunos = alunos.split(';')
            if pesquisa == alunos[0]:
                media_g = (float(alunos[2]) + float(alunos[3]) + float(alunos[4]) + float(alunos[5])) / 4
                print(f"A media da Aluno(a) {alunos[0]} é {media_g}")
            else:
                print("Esse aluno não existe, tente novamente.")
                return

def cacau():
    verificar = str(input("Digite o nome do aluno que quer ver se passou: "))
    with open('alunos.txt', 'r', encoding='utf-8') as file:
        leitura = file.readlines()
        for alunos in leitura:
            alunos = alunos.strip()
            alunos = alunos.split(';')
            if verificar == alunos[0]:
                v = str(alunos[6])
                if v == "Aprovado":
                    print(f"O aluno está {alunos[6]}, ele passou")
                else:
                    print(f"O aluno está {alunos[6]},ele não passou")

def turmas():
    vturma = str(input("Digite o a turma do aluno: "))
    with open('alunos.txt', 'r', encoding='utf-8') as file:
        leitura = file.readlines()
        for alunos in leitura:
            alunos = alunos.strip()
            alunos = alunos.split(';')
            