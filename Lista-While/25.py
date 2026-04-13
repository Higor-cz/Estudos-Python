n1=input('Telefonou para a vítima?(Sim ou Não): ')
n2=input('Esteve no local do crime?(Sim ou Não): ')
n3=input('Mora perto da vítima?(Sim ou Não): ')
n4=input('Devia para a vítima?(Sim ou Não): ')
n5=input('Já trabalhou com a vítima?(Sim ou Não): ')
crime=0
if n1 == 'Sim':
    crime += 1
if n2 == 'Sim':
    crime += 1
if n3 == 'Sim':
    crime += 1
if n4 == 'Sim':
    crime += 1
if n5 == 'Sim':
    crime += 1
if crime == 5:
    print('Essa pessoa é o Assassino')
elif crime >= 3 and crime < 5:
    print('Essa pessoa é Cúmplice')
elif crime == 2:
    print('Essa pessoa é Suspeita')
else:
    print('Essa pessoa é Inocente')