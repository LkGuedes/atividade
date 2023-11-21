#4)	Uma ótica quer fazer um desconto diferenciado com base na idade do usuário em um modelo de óculos que
# custa R$200,00.O desconto será igual a idade do usuário, porém o desconto mínimo será 10% e o desconto
# máximo será de 80%. Faça um programa que pergunte a idade do usuário e então mostre o valor final do
# óculos e o desconto adquirido.

# Solicita a idade do usuário
idade = int(input("Informe sua idade: "))
oculos = 200
desconto = 0.1

if idade <10 :
    desconto = desconto

elif idade >= 80 :
    desconto = 0.8
else :
    desconto = idade /100

valor_total = oculos -(oculos * desconto)

print(f'Seu desconto e de {valor_total}')




