# 14. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
p = 0
i = 0
x = 0 
while x < 10:
    x += 1
    n = float(input(f'Digite o {x} número: '))
    if n % 2 == 0:
        p += 1
    elif n % 2 != 0:
        i += 1
print(f'Entre os 10 números, {p} foram pares e {i} foram impares.')