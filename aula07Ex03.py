

cpf = int(input('Informe o seu CPF'))

cpf = cpf.replace('.','')
cpf = cpf.replace('-','')

if len(cpf) !=11 or cpf.isdigit() == False:
    print('Digite um CPF valido!!!')
    cpf_digito = int(cpf[-2:-1])

cpf = cpf[:9]

#verificacao do CPF

soma = 0
numero = 10
for digito in cpf:
    soma+=int(digito)*numero
    numero -= 1

soma = soma*10

soma = soma%11

if soma >0:
    soma == 0
else:
    soma = soma

if soma == cpf_digito:
    print('CPF VALIDO')
else:
    print('CALCELADO')
