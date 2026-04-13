sim = 0
nao = 0
nome = None
resposta = None
while sim < 12 and (nome != 'nycole' or resposta != 'sim'):
    nome = input('Qual teu nome meu amor? ')
    resposta = input('Bora dançar, cuida!!!')
    if resposta == 'sim':
        sim = sim + 1
    else:
        nao = nao + 1
perc = (sim / (sim+nao))*100
print('Risadinha venceu na vida, mas a mulher dele ta puta...')
print(f'Mas ele sofreu a humilhação de {nao} não.')
print(f'Seu percentual de sucesso foi de {perc:.2f}%')