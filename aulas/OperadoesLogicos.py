#OPERADORES
"""
   ATRIBUIÇÃO
   = ->  variavel = 10
   ! = NÃO, NOT, CONTRÁRIO...
   SIM -> !SIM = NÃO

   idade = 18

    COMPARAÇÃO
    esperar uma resposta de True iu False
   != se for diferente retornar True, se for igual retorna False
   == -> se for diferente retornar False, se for igual vai retornar True
   > -> se for maior retorna True, se for menor retorna False
   < -> se for menor retorna False, se for igual retorna True
   >= -> se for maior retorna True, contrario retorna False
   <= -> se for menor retorna True, contrario retorna False

   PARA MAIS COMPARAÇÕES
   and -> se todas as comparações forem True, retorna True
   idade - 18

   idade == 18 and idade > 18 -> False
           True         False
"""

idade = 18

#adulto = 18
#idosos = 65
#crianças = entre 0 e 10
#adolecente = entre 11 e 17

idade >= (idade <= 17 and idade >= 11 or idade == 33)

# print(idade != 18) # False
