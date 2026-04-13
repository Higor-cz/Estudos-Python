h=float(input('Digite quantas horas foram trabalhadas: '))
sph=float(input('Digite quanto você ganha por hora: '))
salario=h*sph
fgts=salario*0.11
sind=salario*0.03
if salario<=900:
    ir=0
    imposto='Isento'
elif salario>900 and salario<=1500:
    ir=salario*0.05
    imposto=5
elif salario>1500 and salario<=2500:
    ir=salario*0.1
    imposto=10
elif salario>2500:
    ir=salario*0.2
    imposto=20
descontos=ir+sind
SalF=salario-descontos
print(f'Salário Bruto: ({sph} * {h})           :R${salario:.2f}')
print(f'(-) IR ({imposto}%)                            :R${ir:.2f}')
print(f'(-) Sindicato (3%)                     :R${sind:.2f}')
print(f'FGTS (11%)                             :R${fgts:.2f}')
print(f'Total de descontos                     :R${descontos:.2f}')
print(f'Salário Liquido                        :R${SalF:.2f}')