from time import sleep
print('Bem vindo a sua lista de compras !!!')

compras = []

while True:
    menu = input('''Escolha uma das opcoes abaixo :
    1--> Adicionar um novo item 
    2--> Remover um item
    3--> Listar itens da Lista
    4--> Sair do Programa
    ''')
    if menu =='1':
        item = input("Digite um item para adicionar a lista ")
        compras.append(item)
        print(f'Foi adicionado {item} a lista de compras ')

    if menu =='3':
        for i in range(len(compras)):
            print(f'{i+1}: {compras[i]}')
            sleep(1)

    if menu == '2':
        escolha = int(input('ESCOLHA UM ITEM PARA DELETAR:'))
        compras.pop(escolha-1)
        print(f'O item foi deletado da lista ')

    if menu == '4':
        print('Voce saiu do programa ')
        break

    else:
        print('Digite uma opcao Valida')



#______________________________________________________________________________________#


























































#lista_de_compras = []

### Função para add um item da lista de compras
#def adicionar_item(item):
#    lista_de_compras.append(item)
#    print(f"{item}foi adicionado a lista de compras")

### Função para remover um item da lista de compras
#def remover_item(item):
#    if item in lista_de_compras:
#        lista_de_compras.remove(item)
#        print(f"{item} foi removido da lista de compras.")
#    else:
#        print(f"{item} não está na lista de compras.")
#
### Função para listar os itens da lista de compras
#def listar_itens():
#    if not lista_de_compras:
#        print("A lista de compras está vazia.")
#    else:
#        print("Itens na lista de compras:")
#        for item in lista_de_compras:
#            print(item)

#while True :
#    mercado = input('1-> Adicionar item | 2->Remover item | 3-> Listar itens')

#    if mercado == '1':
#        item = input('Digite o nome do item que sera adiconado a lista')

#    elif mercado == '2' :
#        item = input( 'Digite o nome do item que sera removido da lista')

#    elif mercado == '3':
#        listar_itens()

#    else:
#        print('Voce Digitou uma opcao invalida. Favor escolhe 1 ou 2 ou 3')


#______________________________________________________________________________________#

