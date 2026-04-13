valor = float(input('Tu quer quanto boy?\n'))
meses = 0
while meses < 12:
    valor = valor * 1.18
    meses = meses + 1
print(f'O valor final foi de {valor}')