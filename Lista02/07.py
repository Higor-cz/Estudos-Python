#Faça um programa que leia 5 números e informe o maior número.
numeroM = True
for i in range(5):
    n = float(input(f'Digite o {i+1} número: '))
    if numeroM == True:
        numeroM = n
    elif n > numeroM:
        numeroM = n
print(f'O maior número é {numeroM}.')