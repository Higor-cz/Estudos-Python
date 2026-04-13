n1=float(input('Digite um número menor que 1000: '))
if n1 >1000:
    print('Número inválido')
else:
    centenas=n1//100
    resto=n1%100
    dezenas=resto//10
    resto=resto%10
    unidades=resto
    print(f'{n1}= {centenas:.0f} centenas, {dezenas:.0f} dezenas,{unidades:.0f} unidades.')