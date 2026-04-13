n1=float('Digite a primeira nota: ')
n2=float('Digite a segunda nota: ')
n3=float('Digite a terceira nota: ')
media=(n1+n2+n3)/3
if media == 10:
    print('Aprovado com distinção')
elif media >= 7 and media<10:
    print('Aprovado')
elif media <7 and media>=0:
    print('Reprovado')
else:
    print('Media inválida')