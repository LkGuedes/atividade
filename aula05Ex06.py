


ano = int(input('Informe o Ano :'))

if (ano % 400 == 0 )or (ano % 4 ==0 and ano % 100 != 0 ) :
    print('Esse ano e Bissesto ')
else:
    print('Esse ano nao e Bissesto')