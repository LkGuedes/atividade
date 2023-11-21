#exercicio 12

#12)	Faça um programa que realize o cadastro de um usuário a partir de seu nome,
# idade, peso, altura que deverão ser informados pelo usuário e exiba a frase:
# Seu nome é ______ e tem ___ caracteres, você tem ___ anos e nasceu no ano de
# ______. Você mede _____cm, pesa ____ Kg e seu IMC é:____. Não esqueça de manter
# uma boa interface com o usuário!!

#*Fórmula do cálculo do IMC: IMC = Peso ÷ (Altura × Altura)
#Peso em KG
#Altura em metros






nome = input("Qual seu nome")
idade = int(input("Qual sua idade ?"))
peso = float(input("Qual  seu peso ?"))
altura = float(input("QUal a sua altura ?"))
# ano = int(input('Informe o ano atual'))

resultado = (2023 - idade)                     #FORMULAS
imc = ((altura * altura)/peso)                 #FORMULAS
caracteres = len(nome)                         # LEN USADO PARA CONTAR CARACTERES DA PALAVRA  (PALAVRA QUE QUER CONTAR )

print('Seu nome e ', nome ,'e tem',caracteres, 'caracteres ,voce tem',idade,'anos e nasceu no ano de',resultado ,
      '.Voce mede ',altura,'cm,pesa ',peso, 'kg e seu IMC e :',imc )