#Faça um programa que leia 5 números e informe o maior número.
i = 0
nm = None
while i < 5:
    i += 1
    n = float(input(f'Digite o {i} número: '))
    if n > nm:
        nm = n
print(nm)