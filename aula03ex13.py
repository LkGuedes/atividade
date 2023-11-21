#exercicio 13

#13)	Um fabricante de tintas quer montar um programa que auxilie o comprador a saber
# quantas latas de tinta ele precisará para pintar sua parede. Monte um programa em python que execute
# esta função a partir dos dados informados pelo usuário (largura e altura), sabendo que cada lata de
# tinta cobre 3m² de parede. Não esqueça de manter uma boa interface com o usuário!!



largura = float(input('QUAL A LARGURA DA PAREDE ?'))
altura = float(input('QUAL A ALTURA DA PAREDE '))

parede = largura *altura

tinta = parede / 3

print('Voce usara ',tinta,'latas de tintas')