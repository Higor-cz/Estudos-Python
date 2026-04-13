saque = float(input('Digite o valor do saque: '))
n100 = saque // 100
resto = saque % 100
n50 = resto // 50
resto %= 50
n10 = resto//10
resto %= 10
n5 = resto // 5
resto %= 5
n1 = resto
if saque < 10 or saque > 600:
    print('Saque inválido')
else:
    print(f'Seram sacadas {n100} notas de cem, {n50} notas de cinquenta, {n10} notas de dez, {n5} notas de cinco e {n1} notas de um.')