nome=input('Diga seu nome: ')
idade=int(input('Diga a idade: '))
salario=float(input('Diga o salario: '))
if nome=='adilson'and idade>32 and salario <= 5000:
    print(f'{nome} foi contratado para o atletico')
else:
    print('Não foi dessa vez')