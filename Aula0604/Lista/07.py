numero = 0
contador = 1
multiplo = False
while numero >= 0:
    numero = int(input(f'Entre com o número {contador} do conjunto: '))
    contador += 1
    if numero % 10 == 0 and numero >=0:
        multiplo = True
if multiplo == True:
    print('Existe um multiplo de 10 neste conjunto!!!')
else:
    print('Não existe um multiplo de 10 neste conjunto!!!')
