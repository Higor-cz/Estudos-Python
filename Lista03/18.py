#18. Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
n = int(input('Insira quantos núemro deseja no seu conjunto: '))
i = 0
soma = 0
maiorn = 0
menorn = 0
while i < n:
    i += 1
    nc = float(input(f'Insira o {i}º digito do conjunto: '))
    soma += nc
    if nc > maiorn:
        maiorn = nc
        dmaior = i
    elif nc < menorn:
        menorn = nc
        dmenor = i
print(f'A soma de todos os digitos é {soma}.')
print(f'O digito {dmaior} é o maior número do conjunto e seu valor é {maiorn}.')
print(f'O digito {dmenor} é o maior número do conjunto e seu valor é {menorn}.')
