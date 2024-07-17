Valor_compra = float(input("coloque o valor de compra total?  "))

if Valor_compra >= 500:
    print("PARABÉNS. VOCÊ GANHOU SUPER DESCONTO DE 30%")

elif Valor_compra >= 250:
    print("PARABÉNS. VOCÊ GANHOU 10% DE DESCONTO, MAS PODE GANHAR 30% SE SUA COMPRA FOR ACIMA DE R$500,00")

else:
    print("poxa, falta pouco para você ganhar 10 de desconto em sua compra")