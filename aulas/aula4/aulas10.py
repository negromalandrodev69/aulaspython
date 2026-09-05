print("Primeira nota do aluno :")
nota1 = float(input())
print("Segunda nota do aluno :")
nota2 = float(input())
print("Numero que o aluno veio nas aulas :")
frequencia = input()
nota_geral = nota1 + nota2 / 2
print("O aluno passou?",  nota_geral >= 5.9 and nota_geral >= 74)