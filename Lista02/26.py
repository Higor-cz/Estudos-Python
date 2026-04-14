#26. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
a = 0
b = 0
c = 0
e = int(input('Qual o total de eleitores?\n'))
for i in range(e):
    voto = int(input('Em quem você deseja votar?(1-Afonso, 2-Bruno, 3-Chico)'))
    if voto == 1:
        a += 1
    elif voto == 2:
        b += 1
    elif voto == 3:
        c += 1
print(f'{a} eleitores votaram em Afonso')
print(f'{b} eleitores votaram em Bruno')
print(f'{c} eleitores votaram em Chico')