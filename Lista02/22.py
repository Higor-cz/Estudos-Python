#22. Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.
#21. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
n = int(input('Insira um número inteiro: '))
teste = 0
primo = False
divisivel = ''
for i in range(n) :
    if i == 0:
        continue
    if n % i == 0:
        teste += 1
        divisivel += str(i) + '|'
if teste == 1:
    primo = True
if primo:
    print(f'O número {n} é primo')
else:
    print(f'O número {n} não é primo')
    print(f'E ele é divisivel por {divisivel + str(n)}')