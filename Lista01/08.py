n1=float(input('Valor do primeiro produto: '))
n2=float(input('Valor do segundo produto: '))
n3=float(input('Valor do terceiro produto: '))
if n1<n2 and n1<n3:
    print('O primeiro produto é o mais barato entre eles.')
elif n2<n1 and n2<n3:
    print('O segundo produto é o mais barato entre eles')
elif n3<n1 and n3<n2:
    print('O terceiro produto é o mais barato entre eles')
else:
    print('Algum dos produtos tem preços iguais.')
