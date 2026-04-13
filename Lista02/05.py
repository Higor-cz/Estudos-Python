#5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
popA = 0
popB = 1
i = 0
while True:
    popA = int(input('Qual a cidade com a menor população\n'))
    txA = float(input('Qual a taxa de crescimento da população?(em %)\n'))
    txA /= 100
    popB = int(input('Qual a cidade com a maior população\n'))
    txB = float(input('Qual a taxa de crescimento da população?(em %)\n'))
    txB /= 100
    while popA < popB :
        popA *= txA+1
        popB *= txB+1
        i += 1
    print(f'Foram nescessario {i} anos para a População da cidade A igualar ou Ultrapassar a População da cidade B')
    repetir = int(input('Deseja repetir o processo?(0-Não, 1-Sim)'))
    if repetir == 1:
        print('Programa encerrado.')
        break
