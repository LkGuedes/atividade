def nome_ao_contrario(nome):
    nome_invertido = ''
    for indice, letra in enumerate(nome):
        nome_invertido+= nome [-indice-1]
    return nome_invertido

#print(nome_ao_contrario('aula'))
#print(nome_ao_contrario('de'))
#print(nome_ao_contrario('python'))


print(nome_ao_contrario('aula de python '))

