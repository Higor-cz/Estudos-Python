#12. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
n1 = int(input('Qual número você deseja ver a tabuada?\n'))
i = 0
while i < 10:
    i += 1
    print(f'{n1} X {i} = {n1*i}')