#23. Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
n = int(input('Insira um número inteiro: '))
primo = False
divisivel = ''
p = ''
for x in range(n):
    teste = 0
    if x == 0:
        continue
    for i in range(x) :
        if i == 0:
            continue
        if x % i == 0:
            teste += 1
            divisivel += str(i) + '|'
    if teste == 1:
        primo = True
        p += str(x) + ' é primo ' + f'| Foram executadas {x} divisões\n'
print(p)