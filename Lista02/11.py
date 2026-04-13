#11. Altere o programa anterior para mostrar no final a soma dos números.
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
soma = 0
if n1 < n2:
    while n1 < n2 - 1:
        n1 += 1
        print(n1,end=' ')
        soma += n1
elif n2 < n1:
    while n2 < n1 - 1:
        n2 += 1
        print(n2,end=' ')
        soma += n2
print('')
print(soma)