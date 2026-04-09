#Faça um programa que leia 5 números e informe o maior número.
i = 0
numerom = True
while i < 5:
    i += 1
    n = float(input(f'Digite o {i} número: '))
    if numerom == True:
        numerom = n
    elif n > numerom:
        numerom = n
print(f'O maior número é {numerom}.')