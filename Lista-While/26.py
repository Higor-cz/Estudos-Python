tipo=input('Qual combustivel escolhido?(A-Alcool,G-Gasolina)\n')
litros=float(input('Quantos litros a serem abastecidos?\n'))
descontoA=0
descontoG=0
if tipo == 'A':
    combustivel='Alcool'
    if litros <= 20:
        descontoA=0.03
    elif litros >20:
        descontoA=0.05  
elif tipo == 'G':
    combustivel='Gasolina'
    if litros <= 20:
        descontoG=0.04
    elif litros >20:
        descontoG=0.06
psA=litros*1.90
pA=psA-(psA*descontoA)
psG=litros*2.50
pG=psG-(psG*descontoG)
if tipo == 'A':
    print(f'O cliente abastesceu {litros} litros de {combustivel} e pagará: R$ {pA:.2f}')
elif tipo == 'G':
    print(f'O cliente abastesceu {litros} litros de {tipo} e pagará: R$ {pG:.2f}')