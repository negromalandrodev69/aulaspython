print("Olá,quanto foi o valor total da compra?")
conta = float(input())
print("Agora quantas pessoas estão na sua mesa?")
pessoas = int(input())
valor_dividido = conta / pessoas
print("O valor total da sua compra foi R$", conta, "e cada pessoa deve pagar R$", valor_dividido)