salario=float(input('Digite seu salário para o reajuste:'))
if salario<=280:
    pr=20
    reajuste=salario*0.2
    salarioR=salario*1.2
elif salario>280 and salario<= 700:
    pr=15
    reajuste=salario*0.15
    salarioR=salario*1.15
elif salario>700 and salario<=1500:
    pr=10
    reajuste=salario*0.1
    salarioR=salario*1.1
elif salario>1500:
    pr=5
    reajuste=salario*0.05
    salarioR=salario+reajuste
else:
    print('Valor informado inválido.')
print(f'O salário antes do reajuste era de R${salario}.')
print(f'A porcetagem do reajuste foi de {pr}%')
print(f'O valor de aumento foi de R${reajuste}')
print(f'O novo salario após o aumento é de R${salarioR}')