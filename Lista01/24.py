n1=float(input('Digite um número: '))
n2=float(input('Digite outro número: '))
op=input('Qual operação deseja realizar? (a-Se o número é par ou impar,b-Se o número é positivo ou negativo,c-Se o número é inteiro ou decimal)')
if op == 'a':
    if n1 % 2 == 0:
        print(f'O número {n1} é par.')
    elif n1 % 2 != 0:
        print(f'O número {n1} é impar.')
    if n2 % 2 == 0:
        print(f'O número {n2} é par.')
    elif n2 % 2 != 0:
        print(f'O número {n2} é impar.')
elif op == 'b':
    if n1 >= 0:
        print(f'{n1} é positivo')
    else:
        print(f'{n1} é negativo')
    if n2 >= 0:
        print(f'{n2} é positivo')
    else:
        print(f'{n2} é negativo')
elif op == 'c':
    if n1 % 1 == 0:
        print(f'O número {n1} é inteiro.')
    elif n1 % 1 != 0:
        print(f'O número {n1} é decimal.')
    if n2 % 1 == 0:
        print(f'O número {n2} é inteiro.')
    elif n2 % 1 != 0:
        print(f'O número {n2} é decimal.')