n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
media=(n1+n2)/2
if media>7 and media<10:
    print('Aprovado')
elif media==10:
    print('Aprovado com distinção')
else:
    print('Reprovado')