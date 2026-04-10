#17. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
inicio = int(input('Qual fatorial deseja saber?\n'))
numero = inicio
fatorial = 1
while numero > 0:
    fatorial *= numero
    numero -= 1
print(f'{inicio}! = {fatorial}')