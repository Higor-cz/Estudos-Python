numero = int(input('Digite um número: '))
repetir = 1
while numero < 0 :
    print('Número inválido!!!')
    numero = int(input('Digite um número: '))
while repetir == 1:
    if numero % 2 == 0:
        print(f'{numero} é par')
    else:
        print(f'{numero} é impar')
    repetir = int(input('Deseja continuar?? ( 0 - Não) (1 - Sim)'))
    if repetir == 1:
        numero = int(input('Digite um número: '))
        while numero < 0 :
            print('Número inválido!!!')
            numero = int(input('Digite um número: '))
print('Tenha um bom dia!')