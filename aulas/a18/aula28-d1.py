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
        media_alunos = []
        aluno_mm = []
        media_maior = 0
        for alunos in leitura:
            alunos = alunos.strip()
            alunos = alunos.split(';')
            if vturma == alunos[1]:
                media = (float(alunos[2]) + float(alunos[3]) + float(alunos[4]) + float(alunos[5])) / 4 # Refazer a media para o proprio metodo
                nome = alunos[0]   # Orientar o nome dos alunos para lista
                media_alunos.append([nome, media])

                if media > maior_media:
                    maior_media = media
                    aluno_mm.append(alunos[0])
                    aluno_mm.append(maior_media)

        len_nome = (len(aluno_mm) - 2)
        len_media = (len(aluno_mm) - 1)
        print(f"A maior maior media foi o aluno {aluno_mm[len_nome]} com a média {aluno_mm[len_media]}")

while True:  # loop infinito
    opcao = int(input("Escolha uma opcao:\n"
            "1) Adicionar aluno\n"
            "2) Listar nomes\n"
            "3) Buscar por nome\n"
            "4) Maior media\n"
            "5) Sair\n"
            "\nDigite: "))

    match opcao:
            case 1:
                add_alunos()
            case 2:
                padronizartxt()
            case 3:
                cacau()
            case 4:
                turmas()
            case 5:
                print("Finalizando sistema...")
                break