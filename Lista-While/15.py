l1=float(input('Digite o lada A do triangulo: '))
l2=float(input('Digite o lada B do triangulo: '))
l3=float(input('Digite o lada C do triangulo: '))
if (l1+l2)>l3 and (l1+l3)>l2 and (l2+l3)>l1:
    if l1==l2 and l1==l3:
        print('É um triangulo equilatero.')
    elif l1==l2 or l1==l3 or l2==l3:
        print('É um triangulo Isóceles.')
    elif l1!=l2 and l1!=l3:
        print('É um triangulo Escaleno.')
else:
    print('Os lados informados não formam um triangulo.')