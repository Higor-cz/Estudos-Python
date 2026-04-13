n1=float(input('Digite um número: '))
n2=float(input('Digite um número: '))
n3=float(input('Digite um número: '))
if n1>n2 and n1>n3:
    if n2>n3:
        print(f'{n1},{n2},{n3}.')
    elif n3>n2:
        print(f'{n1},{n3},{n2}.')
    else:
        print(f'{n1} é maior e {n2} e {n3} são iguais.')
elif n2>n1 and n2>n3:
    if n1>n3:
        print(f'{n2},{n1},{n3}.')
    elif n3>n1:
        print(f'{n2},{n3},{n1}.')
    else:
        print(f'{n2} é maior e {n1} e {n3} são iguais.')
elif n3>n1 and n3>n2:
    if n1>n2:
        print(f'{n3},{n1},{n2}.')
    elif n2>n1:
        print(f'{n3},{n2},{n1}.')
    else:
        print(f'{n3} é maior e {n2} e {n1} são iguais.')