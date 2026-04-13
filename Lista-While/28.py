tipo=input('Qual tipo de carne?(F-Filé Duplo A-Alcatra P-Picanha\n')
quantidade=float(input('Quantos quilos de carne?\n'))
metodo=input('Qual metodo de pagamento?(D-Dinheiro C-Cartão Tabajara)\n')
if tipo == 'F':
    Carne = 'Filé Duplo'
    if quantidade <= 5:
        valor = quantidade * 4.90
    elif quantidade > 5:
        valor = quantidade * 5.80
elif tipo == 'A':
    Carne = 'Alcatra'
    if quantidade <= 5:
        valor = quantidade * 5.90
    elif quantidade > 5:
        valor = quantidade * 6.80
elif tipo == 'P':
    Carne = 'Picanha'
    if quantidade <= 5:
        valor = quantidade * 6.90
    elif quantidade > 5:
        valor = quantidade * 7.80
if metodo == 'C':
    desconto=valor*0.05
    precoT=valor-desconto
    Pagamento='Cartão'
else:
    desconto = 0
    precoT = valor
    Pagamento = 'Dinheiro'
print(f'Tipo de carne           {Carne}')
print(f'Quilos                  {quantidade:.2f}kg')
print(f'Valor total da Compra   R${valor:.2f}')
print(f'Tipo de pagamento       {Pagamento}')
print(f'Valor descontado        R${desconto:.2f}')
print(f'Total a pagar           R${precoT:.2f}')