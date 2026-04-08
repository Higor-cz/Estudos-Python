#Faça um programa que leia 5 números e informe o maior número.
i = 0
nm = True
while i < 5:
    try:
        i += 1
        n = float(input(f'Digite o {i} número: '))
        if nm == True:
            nm = n
        elif n > nm:
            nm = n
    except:
        print('TA VIÇANDO CARAI')
print(nm) 