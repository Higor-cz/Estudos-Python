n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
n3 = float(input('Digite sua terceira nota: '))
media=(n1+n2+n3)/3
if media>=7:
    print('Você foi aprovado')
else:
    print('Você foi pra final.')
    notaf=float(input('Digita sua nota na final'))
    if notaf >=7:
        print('Você foi aprovado na final')
    else:
        print('Você foi reprovado.')