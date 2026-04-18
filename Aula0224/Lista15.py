ganho=float(input('Digite quando ganha por hora: '))
horas=float(input('Digita quantas horas foram trabalhadas no mês: '))
bruto=horas*ganho
Sind=bruto*5/100
Imposto=bruto*11/100
inss=bruto*8/100
Liquido=bruto-(Sind+inss+Imposto)
print(f'+ Salário Bruto:R$ {bruto:.2f}')
print(f'- IR (11%):R$ {Imposto:.2f}')
print(f'- INSS (8%):R$ {inss:.2f}')
print(f'- Sindicato (5%):R$ {Sind:.2f}')
print(f'= Salário Liquido:R$ {Liquido:.2f}') 