def letra(texto):
    texto = texto.replace('A','4')
    texto = texto.replace('a', '4')
    texto = texto.replace('B','8')
    texto = texto.replace('E','3')
    texto = texto.replace('I','1')
    texto = texto.replace('O','0')
    texto = texto.replace('T','7')

    return texto
print(letra('aaa'))
