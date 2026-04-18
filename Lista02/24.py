#24. Faça um programa que calcule o mostre a média aritmética de N notas.
n = int(input('Quantas notas serão avaliadas?\n'))
i = 0
soma = 0
while i < n:
    i += 1
    nota = float(input(f'Insira a {i}ª nota: '))
    soma += nota
media = soma/n
print(f'A media dessas {n} notas foi de: {media}')