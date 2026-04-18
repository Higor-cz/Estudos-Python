h=float(input("Digite sua altura: "))
p=float(input('Digite seu peso: '))
imc=p/(h**2)
if imc < 25:
    print('seu imc está normal')
else:
    if imc < 30:
        print('Você está com Sobrepeso')
    else:
        print('Você está Obeso')

