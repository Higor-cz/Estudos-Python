#13. Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.
n1 = int(input('Digite a Base: '))
n2 = int(input('Digite o Expoente: '))
i = 0
multi = n1
while i < n2 - 1:
    i += 1
    multi *= n1
print(multi)