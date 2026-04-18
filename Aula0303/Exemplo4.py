Chave=input('Você possui a chave?(S/N): ').upper()
mala=input('Você é malandro?(S/N): ').upper()
corage=input('Você possui coragem?(S/N): ').upper()
if Chave=='S' or mala=='S' and corage=='S':
    print('O carro é meu!!!')
else:
    print('A policia lhe prendeu!!!')