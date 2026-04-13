#21. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
n = int(input('Insira um número inteiro: '))
teste = 0
primo = False
i = 0
while i < n:
    i += 1
    if n % i == 0:
        teste += 1
    if teste > 2:
        break
if teste == 2:
    primo = True
if primo:
    print(f'O número {n} é primo')
else:
    print(f'O número {n} não é primo')
    
