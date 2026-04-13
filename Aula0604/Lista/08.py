vetor = int(input('Quantas coordenadas deseja no seu vetor?\n'))
n = 0
ortante = True
while n < vetor:
    n+=1
    numero = int(input(f'Digite a coordenada {n}: '))
    if numero < 0:
        ortante = False
if ortante == False:
    print('O vetor não se encontra na primeira Ortante!!!')
else:
    print('O vetor se encontra na primeira ortante!!!')