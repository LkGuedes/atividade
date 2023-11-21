# EXERCICIO 5

#5)	Uma empresa pretende fazer um reajuste salarial para os funcionários e precisa da sua ajuda para criar
# um programa. Ficou definido os seguintes reajustes:
#•	Salário Abaixo de R$1.500,00  Aumento de 25%
#•	Salário Entre de R$1.500,00 e R$1.999,99  Aumento de 20%
#•	Salário Entre de R$2.000,00 e R$2.999,99  Aumento de 15%
#•	Salário Entre de R$3.000,00 e R$4.999,99  Aumento de 10%
#•	Salário Igual ou Acima de R$5.000,00  Aumento de 5%

#Faça um programa que pergunte ao usuário qual seu Salário Atual e mostre ao usuário:
#1.	O salário atual;
#2.	A porcentagem do reajuste;
#3.	O aumento em R$;
#4.	O salário final após o reajuste.

# Solicita a idade do usuário
salario = int(input("Digite o seu salario atual sem montos e virgulas : "))

aumento = 0.25

if salario < 1500 :
    aumento = aumento

elif 1500 >= salario <=1999 :
    aumento = 0.20

elif 2000 >= salario <= 2999:
    aumento = 0.15

elif 3000>= salario <=4999:
    aumento = 0.10

elif salario >= 5000 :
    aumento = 0.5

porcentagem = aumento * 100   #informa a porcentagem
valor_total = (salario * aumento)  #informa o valor total do reajuste
aumento_salario = valor_total + salario #informa o valor total com reajuste


print('O seu salario atual e R$ ',salario)
print('A porcentagem de reajuste e de ', porcentagem,'%')
print('Voce teve um aumento de R$',valor_total)
print('Voce ganhara agora R$ ', aumento_salario)

#print(f'O salaio final e de :{aumento_salario}')  # Outra forma de fazer o print




