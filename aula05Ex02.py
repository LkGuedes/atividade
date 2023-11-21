#exercicio 2
#2)	Uma empresa de transporte público quer fazer um sistema automático para identificar
# se o usuário terá gratuidade no transporte ou não. Faça um programa que pergunte a idade
# do usuário, se ele tiver 65 anos ou mais irá informar que ele tem gratuidade no transporte.
idade = int(input('Informe sua idade ')) # Pergunta int para numeros inteiros

if idade >= 65: # >= para maior ou igual  sempre dois pontos depois de if e else 
    print('Voce tem gratuidade no transporte ')
else :
    print('Voce deverar pagar o transporte')

