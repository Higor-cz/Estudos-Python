preco=float(input('Valor da compra: '))
metodo=input('Metodo de pagamento: ').upper()
Desconto=0
if metodo=='PIX' or metodo== 'AVISTA':
    Desconto=preco*12/100
precof=preco-Desconto
print(f'Total da compra foi de : R$ {preco}')
print(f'O total do desconto foi de: R${Desconto}')
print(f'O valor final é: R${precof}')