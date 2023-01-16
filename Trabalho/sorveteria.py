print('Bem-vindos a Sorveteria do Pedro Ernesto F. Romero RU:3072172')
print('------------------------------CARDÁPIO------------------------------')
print('CÓDIGO | DESCRIÇÃO  | SORVETE (P) (500ml)    |    SORVETE (M) (1000ml) |   SOVERTE (G) (2000ml) |')
print('  TR   |Tradicional |      R$ 6.00           |      R$ 10.00           |      R$ 18.00          |')
print('  ES   | Especial   |      R$ 7.00           |      R$ 12.00           |      R$ 21.00          |')
print('  PR   | Premium    |      R$ 8.00           |      R$ 14.00           |      R$ 23.00          |')

                            #(P)=500 ml | (M)=1 Litro | (G)=2 Litros
tamanho = ["P", "M", "G"]

#-----------------------------------------------------------------------------------------------------------
codigos = {"TR": [6.00, 10.00, 18.00],

# TR=SABORES TRADICIONAIS

          "ES": [7.00, 12.00, 21.00],

# ES=SABORES ESPECIAIS

          "PR": [8.00, 14.00, 23.00]}

# PR=SABORES PREMIUM
#--------------------------------------------------------------------------------------------------------------
compra = []

# pedindo os dados

while True:

   qual_tamanho = input("Qual o tamanho do sorvete desejado?(P/M/G) ")

   qual_sabor = input("Qual o código do sorvete desejado?(TR/ES/PR) ")

   if qual_tamanho in tamanho and qual_sabor in codigos:

       pedido = codigos[qual_sabor][tamanho.index(qual_tamanho)]

       compra.append(pedido)

       algo_mais = input ("Deseja pedir algo mais?"

                          "\nDigite S para sim ou N para não. ")

       if algo_mais == "S":

           continue

       else:

           break

   else:

       print("TAMANHO ou CÓDIGO inválido(s)")

       continue

print ("Valor total da compra:", "R$",sum(compra))

