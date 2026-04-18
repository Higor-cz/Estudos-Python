h=float(input("Digite sua altura: "))
p=float(input('Digite seu peso: '))
imc=p/(h**2)
if imc < 25:
    print(f'Seu indice é de {imc} e está com peso normal')
else:
    print(f'Seu indice é de {imc} e está com sobrepeso')