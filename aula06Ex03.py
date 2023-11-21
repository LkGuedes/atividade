#3)	Faça um jogo de Pedra, Papel e Tesoura.
#No qual você digitará a letra P para jogar Papel,
# a letra R para jogar Pedra e a letra T para jogar Tesoura.
#Você jogará contra o computador e contabilizara o
# número de vitórias, empates e derrotas.
import random as rd

opcaoes = 'P', 'R', 'S', 'T'

maquina = rd.choice(opcaoes) #choice serve para a maquina mesmo escolhe aleatoriamente

vitoria = 0
empate = 0
derrota = 0

while True:
    jogo = input('Escolha P = Papel ,R = Pedra, T = Tesoura, S = Sair ')

    print('Maquina escolheu = ',maquina)
    maquina = rd.choice(opcaoes)

    if jogo == 'S' or jogo == 's':
        print('Voce saiu do Jogo')
        break

    elif (maquina == 'P') or ( maquina == 'R' ) or (maquina == 'T') :
        print('Voce impatou ')
        empate +=1

    elif (maquina == 'P'and jogo == 'R') or (maquina == 'R' and jogo == 'T') or (maquina == 'T'and jogo == 'P'):
        print('Voce Perdeu')
        derrota +=1

    elif (jogo == 'P' and maquina == 'R') or (jogo == 'R' and maquina == 'T') or (jogo == 'T' and maquina == 'P'):
        print('Voce Ganhou')
        vitoria +=1

print('Vitorias =',vitoria,'\n Derrotas = ',derrota,'\n Empates = ',empate) #\n serve para quebra a linha
