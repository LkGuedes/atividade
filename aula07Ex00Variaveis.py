
#  Lista  | armazena itens de forma ordenada.

#EXEMPLO 01
#lista_de_compras = ["feijao ","Carne ","batata","Maca","ovo"]

#print('Minha lista de compras ')
#print(lista_de_compras)

#print('\nminha primeira compra ',lista_de_compras[0])

#___________________________________________________________________

#lista_gulosemas = ["chocolate","bis","Bolacha"]
#lista_bebidas = ["coca","suco","gatorade"]
#lista_de_compras = [lista_gulosemas,lista_bebidas,"feijao"]

#print('Minha lista de compra: ')
#print(lista_de_compras)

#___________________________________________________________________


# Cria uma lista vazia para a lista de compras
lista_de_compras = []


# Função para adicionar um item à lista de compras
def adicionar_item(item):
    lista_de_compras.append(item)
    print(f"{item} foi adicionado à lista de compras.")


# Função para remover um item da lista de compras
def remover_item(item):
    if item in lista_de_compras:
        lista_de_compras.remove(item)
        print(f"{item} foi removido da lista de compras.")
    else:
        print(f"{item} não está na lista de compras.")


# Função para listar os itens da lista de compras
def listar_itens():
    if not lista_de_compras:
        print("A lista de compras está vazia.")
    else:
        print("Itens na lista de compras:")
        for item in lista_de_compras:
            print(item)


# Loop principal
while True:
    print("\nOpções:")
    print("1 - Adicionar item à lista")
    print("2 - Remover item da lista")
    print("3 - Listar itens da lista")
    print("4 - Sair")

    escolha = input("Escolha uma opção (1/2/3/4): ")

    if escolha == '1':
        item = input("Digite o item que deseja adicionar: ")
        adicionar_item(item)
    elif escolha == '2':
        item = input("Digite o item que deseja remover: ")
        remover_item(item)
    elif escolha == '3':
        listar_itens()
    elif escolha == '4':
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

