n1=float(input('Digite um número: '))
n2=float(input('Digite um número: '))
n3=float(input('Digite um número: '))
if n1>n2 and n1>n3:
    if n2>n3:
        print(f'{n1} é o maior entre eles, e o {n3} é o menor.')
    elif n3>n2:
         print(f'{n1} é o maior entre eles, e o {n2} é o menor.')
elif n2>n1 and n2>n3:
   if n1>n3:
        print(f'{n2} é o maior entre eles, e o {n3} é o menor.')
   elif n3>n1:
         print(f'{n2} é o maior entre eles, e o {n1} é o menor.')
elif n3>n1 and n3>n2:
    if n2>n1:
        print(f'{n3} é o maior entre eles, e o {n1} é o menor.')
    elif n1>n2:
         print(f'{n3} é o maior entre eles, e o {n2} é o menor.')
