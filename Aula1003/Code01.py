resposta= input('você esta conectado a internet?')
if resposta== 'sim':
    status= True
else:
    status = False
if not status:
    print('você precisa pegar a senha do wifi com Ludgero.')