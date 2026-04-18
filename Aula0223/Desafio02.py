Compra=float(input("Qual o valor da compra?"))
Desconto=float(input("Qual a porcentagem do desconto?"))
ValorDescontado=Compra*Desconto/100
ValorFinal=Compra-Desconto
print("Valor da compra: ",Compra,"R$")
print("Valor do desconto: ",Desconto,"%")
print("Valor descontado: ",ValorDescontado,"R$")
print("Valor total: ",ValorFinal,"R$")
