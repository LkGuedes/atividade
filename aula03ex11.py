# EXERCICIO 11 converter graus celsius em farenheit

#Faça um programa para converter Graus Celsius em Farenheit informado pelo usuário:
#Escala: 0 ~ 100 ºC         32 ~ 212 ºF


valor = int(input('Informe o valor em Graus celsius'))

resultado = ((valor * 9/5) + 32)  # formula de conversao

print('O resultado em Farenheit e', resultado)