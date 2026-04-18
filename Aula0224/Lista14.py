peso=float(input('Digita o peso dos peixes: '))
excesso=peso-50
if excesso> 0:
    multa=excesso*4
    print(f'A quantidade pescada foi de {peso:.2f}KG, a quantidade em excesso é {excesso:.2f}KG, e o valor da multa a ser pago é: {multa:.2f}R$')
else:
    multa=0
    print(f'A quantidade pescada foi de {peso:.2f}Kg, não houve execedente na pesca.')
