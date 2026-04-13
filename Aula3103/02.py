idade = 0
soma = 0
qtde = 0
while idade >= 0:
    idade = int(input('Qual sua idade? '))
    soma = soma + idade
    qtde = qtde + 1
if qtde -1 > 0:
    media = soma / (qtde - 1)
    print(f'QTDE: {qtde - 1}')
    print(soma)
    print(media)
else:
    print('nenhum usuário digitou idade válida')
