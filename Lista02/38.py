salario = float(input('Digite seu salario\n'))
ano = int(input('Qual ano você começou a trabalhar?\n'))
taxa = 0.015
while ano < 2026:
        salario *= 1+taxa
        taxa *= 2
        ano += 1
taxaAtual = taxa / 2
if ano == 2026:
      taxaAtual = 0

print(f'A taxa atual é de {taxaAtual}')
print (f'Seu salario atual é {salario}')