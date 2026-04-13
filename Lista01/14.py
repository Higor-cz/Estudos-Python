n1=float(input('Digite sua primeira nota: '))
n2=float(input('Digite a segunda nota: '))
media=(n1+n2)/2
if media>=9 and media<=10:
    conceito='A'
elif media>=7.5 and media<9:
     conceito='B'     
elif media>=6.0 and media<7.5:
      conceito='C'       
elif media>=4.0 and media<6.0:
      conceito='D'
elif media>=0.0 and media<4.0:
     conceito='E'
else:
     print('As notas inseridas são inválidas.')
if conceito=='A'or conceito=='B'or conceito=='C':
      print(f'Sua media foi {media}, conceito {conceito}')
      print('Aprovado')
elif conceito=='D'or conceito=='E':
      print(f'Sua media foi {media}, conceito {conceito}.')
      print('Reprovado')
else:
     print('Notas inválidas!!')