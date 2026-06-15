#Faça um programa que leia e valide as seguintes informações:
#a. Nome: maior que 3 caracteres;
#b. Idade: entre 0 e 150;
#c. Salário: maior que zero;
#d. Sexo: 'f' ou 'm';
#e. Estado Civil: 's', 'c', 'v', 'd';
while True:
    nome = input('Qual seu nome?\n')
    if len (nome) < 3:
        print ('O nome deve ter mais que 3 caracteres')
        continue
    while True:
        idade = int(input('Qual sua idade?\n'))
        if idade < 0 or idade > 150:
            print('Idade inválida')
            continue
        else:
            break
    while True:
        salario = float(input('Qual seu salario?\n'))
        if salario <= 0:
            print('Salário inválido!!')
            continue
        else:
            break
    while True:
        genero = input('Qual o seu gênero?(f- feminino, m- masculino)\n').lower()
        if genero == 'f':
            sexo = 'Feminino'
        elif genero == 'm':
            sexo = 'Masculino'
        else:
            print('Genero invalido')
            continue
        break
    while True:
        estdcv = input('Qual seu estado civil?(c- casado, s- solteiro, v-viuvo, d-divorciado)\n')
        if estdcv == 'c':
            civil = 'Casado'
        elif estdcv == 's':
            civil = 'Solteiro'
        elif estdcv == 'v':
            civil = 'Viuvo'
        elif estdcv == 'd':
            civil = 'Divorciado'
        else:
            print('Estado Civil inválido!!')
            continue
        break
    break
print(nome)
print(idade)
print(salario)
print(sexo)
print(civil)