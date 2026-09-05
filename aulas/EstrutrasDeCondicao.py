#IF e ELSE -> SE e SENÃO

#CASE SENSITIVE -> E != e

idade = int(input('Digte sua idade :'))

# criando uma condição na execução do código
if idade >= 18: # execute SE a resposta boleana for True
    if idade >= 65:
         print("Desculpa senhor, você não pode entrar nessa balada")
    else:
         print("Você pode entrar nessa balada.")
elif idade < 5: # ElSE + IF -> elif
    print("Além de não poder entrar, você é menor de idade")
else:
    print("Você não pode entrar, é menor e idade.")

nome = input('Digte seu nome :')

if nome == "":
    print("Por favor digite um nome valído.")
else:
    print("Ola"+ nome + "! Seja bem vindo a nossa balada.")
