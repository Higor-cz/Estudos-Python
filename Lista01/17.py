ano = int(input('Digite um ano: '))
test1 = ano % 4
test2 = ano % 100
test3 = ano % 400
if ano % 4 == 0 and not ano%100 == 0 or ano % 4 == 0 and ano % 400 == 0:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')