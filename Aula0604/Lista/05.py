numero = int(input('Digite um número: '))
soma = 0
while numero != -1:
    if numero < 21 or numero > 70:
        soma = soma + numero
    numero = int(input('Digite um número: '))