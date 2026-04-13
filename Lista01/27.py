pesoMa=float(input('Quantos quilos de maça?\n'))
pesoMo=float(input('Quantos quilos de morango?\n'))
if pesoMa <= 5:
    precoMa = pesoMa * 1.80
elif pesoMa > 5:
    precoMa = pesoMa * 1.50
if pesoMo <= 5:
    precoMo = pesoMo * 2.50
elif pesoMo > 5:
    precoMo = pesoMo * 2.20
precoT=precoMa+precoMo
if (pesoMo+pesoMa) > 8 or (precoT) > 25:
    desconto = 0.1
else:
    desconto = 0
precoF=precoT-(precoT*desconto)
print(f'O total da compra foi de: R$ {precoF:.2f}')