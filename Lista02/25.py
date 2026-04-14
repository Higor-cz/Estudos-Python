#25. Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
n = int(input('Quantas pessoas serão avaliadas?\n'))
i = 0
soma = 0
while i < n:
    i += 1
    idade = float(input(f'Insira a idade da {i}ª pessoa: '))
    soma += idade
media = soma/n
if media > 0 and media <= 25:
    print('A turma é jovem.')
elif media > 25 and media <= 60:
    print('A turma é adulta.')
else:
    print('A turma é idosa.')