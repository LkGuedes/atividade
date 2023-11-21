#Ex 01

#1)	Faça um programa para adivinhar um número de 1 a 10000.
#Se você errar o computador deverá responder se é mais ou menos.
#Se você errar 10 vezes você perde o jogo.

import  random as rd

numero = rd.randint(1,1000)
tentativas = 0
limite = 10

while tentativas < limite :

    valor = int(input('Tente adivinha o Numero de 1 a 1000 '))

    if valor < numero :
        print('NUmero e Maior ')
    elif valor > numero :
        print('NUmero e menor ')
    else:
        print("Você acertou o número :" ,numero)
        break

if limite == tentativas:
    print('Voce perdeu ')



