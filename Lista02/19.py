#19. Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
n = int(input('Insira quantos núemro deseja no seu conjunto: '))
i = 0
soma = 0
maiorn = 0
menorn = 0
while i < n:
    i += 1
    nc = float(input(f'Insira o {i}º digito do conjunto: '))
    if nc < 0 or nc > 1000:
        print('Número inválido!')
        i -= 1
        continue
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