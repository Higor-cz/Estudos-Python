#8. Faça um programa que leia 5 números e informe a soma e a média dos números.
i = 0
soma = 0
while i < 5 :
    i += 1
    numero = float(input(f'Digite o {i}º número'))
    soma += numero
    media = soma/i
print(f'A soma dos números é: {soma}')
print(f'A media dos números é: {media}')