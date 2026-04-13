a=float(input('Digite o valor de a: '))
if a!=0:
    b=float(input('Digite o valor de b: '))
    c=float(input('Digite o valor de c: '))
    delta=(b**2)-(4*a*c)
    if delta==0:
        x1=(-b+delta**(1/2))/ (2*a)
        print('A equação possui uma raiz real.')
        print(f'A raiz é {x1}.')
        print('Programa encerrado.')
    elif delta>0:
        x1=(-b+delta**(1/2))/ (2*a)
        x2=(-b-delta**(1/2))/ (2*a)
        print('Delta é positivo, então a equação possui duas raizes reais.')
        print(f'A primeira raiz é {x1}.')
        print(f'A segunda raiz é {x2}.')
        print('Programa encerrado.')
    else:
        print('Delta negativo, não existe raizes reais.')
        print('Programa encerrado.')
else:
    print('Não existe raizes reais')
    print('Programa encerrado.')