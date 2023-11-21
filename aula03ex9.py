# EXERCICIO 9

#9)	Um professor gostaria um programa para auxiliá-lo a montar a média final de seus alunos.
# Sabendo que são 2 notas por semestre, monte um programa que através das notas informadas pelo
# usuário mostre a sua média final. Não esqueça de manter uma boa interface com o usuário!!

nota_01 = float(input('Informe a primeira nota do primeiro semestre  '))  # INT numeros inteiros
nota_02 = float(input('Informe a segunda nota do primeiro semestre  '))   # FLOAT numeros quebrados 2,1
nota_03 = float(input('informe a primera nota do segundo semestre'))
nota_04 = float(input('informe a segunda nota do segundo semestre'))

resultado_01_semestre = (nota_02 + nota_01)
resultado_02_semestre = (nota_03 + nota_04)

resultado_final = ((resultado_01_semestre + resultado_02_semestre) / 2)

print('Sua media final e ',resultado_final)























