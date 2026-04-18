idade=float(input('Qual sua idade: '))
saldo=float(input('Qual o valor do seu saldo: '))
VIP=(input('Você possui Cartão VIP?(S / N): ')).upper()
if idade>=25 and saldo>=1000 or VIP=='S':
    print('Bem vindo, aceita um café?')
else:
    print('Cai fora malandro')
