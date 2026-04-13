dia=float(input('Insira um dia(dd): '))
mes=float(input('Insira um mês(mm): '))
ano=float(input('Insira um ano(aaaa): '))
if ano % 4 == 0 and not ano%100 == 0 or ano % 4 == 0 and ano % 400 == 0:
    if mes == 1 or mes == 3 or mes == 5 or mes == 1 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia > 0 and dia <= 31:
            print(f'{dia:.0f}/{mes:.0f}/{ano:.0f} é uma data válida')
        else:
            print('Data inválida')
    elif mes==2:
        if dia > 0 and dia <= 29:
            print(f'{dia:.0f}/{mes:.0f}/{ano:.0f} é uma data válida')
        else:
            print('Data inválida')
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia > 0 and dia <= 30:
            print(f'{dia:.0f}/{mes:.0f}/{ano:.0f} é uma data válida')
        else:
            print('Data inválida')
    else:
        print('Data inválida')
elif ano >= 0:
    if mes == 1 or mes == 3 or mes == 5 or mes == 1 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia > 0 and dia <= 31:
            print(f'{dia:.0f}/{mes:.0f}/{ano:.0f} é uma data válida')
        else:
            print('Data inválida')
    elif mes==2:
        if dia > 0 and dia <= 28:
           print(f'{dia:.0f}/{mes:.0f}/{ano:.0f} é uma data válida')
        else:
            print('Data inválida')
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia > 0 and dia <= 30:
            print(f'{dia:.0f}/{mes:.0f}/{ano:.0f} é uma data válida')
        else:
            print('Data inválida')
    else:
        print('Data inválida')
else:
    print('Data inválida')