dia = int(input('Informe o DIa '))
mes = int(input('Informe um mes '))
ano = int(input('Informe um ano '))

bissesto = (ano % 400 == 0 ) or (ano % 4 ==0 and ano % 100 != 0 )

if dia <1 or mes <1 or ano <1:
    print('Voce informou uma data inexistente. Favor digitar uma dara Existente ')

elif dia >=1 or dia <=31 and mes >=1 or mes <=12 and ano >=1:
    print("Data válida.")

elif( mes ==1) or (mes ==3) or (mes ==5 )or (mes ==7 )or (mes ==8)or (mes ==10)or (mes ==12) and (dia <= 31) :
    print("Data válida.")

elif( mes ==4) or (mes ==6) or (mes ==9) or (mes ==11) and (dia <= 30) :
    print("Data válida.")

elif (mes == 2 ) and (dia <= 29) and ano == bissesto:
    print(' Ano bissesto')

if bissesto == True :
    print('Esse ano e Bissesto ')

else :
    print('Esse ano nao e Bissesto')
