#3)	Faça um programa que pede duas notas de um aluno. Em seguida ele deve calcular a média do aluno e dar o seguinte resultado:
#•	Aprovado  Acima de 7
#•	Reprovado  Abaixo de 5
#•	Recuperação  Entre 5 e 7



nota = float(input('Informe sua primeira nota !'))
nota_2 = float(input('Informe sua segunda nota !'))

media =(( nota + nota_2 )/2)

if media >= 7 :
    print('Aprovado')
elif media < 5:
    print('Reprovado')
else :
    print('Recuperacao')