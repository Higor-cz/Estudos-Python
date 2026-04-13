#20. Altere o programa de cálculo do fatorial(questão 17), permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
while True:
    inicio = int(input('Qual fatorial deseja saber?\n'))
    numero = inicio
    fatorial = 1
    while numero > 0 and numero < 16:
        fatorial *= numero
        numero -= 1
    if inicio <= 0 or inicio >= 16:
        print('Fatorial inválido inserido, programa encerrado!!')
        break
    else:
        print(f'{inicio}! = {fatorial}')