import random

numero_aleatorio = random.randint(1,1000)

tentativas = 0
while tentativas <10 :
    print(f'Voce tem{10 - tentativas } tentativas')
    chute = int(input('Digite um numero de 1 a 1000 :'))

    if chute == numero_aleatorio:
        print('Parabens Voce acertou o numero ')
        break

    elif chute < numero_aleatorio:
        print('O numero e Maior')
        tentativas = tentativas+1

    elif chute > numero_aleatorio:
        print('O numero e Menor ')
        tentativas = tentativas+1

    else:
        print(f'Voce perdeu =/acabaram as tentativas. O numero era {numero_aleatorio}')