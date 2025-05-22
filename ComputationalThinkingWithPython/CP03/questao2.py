import os

estoque = {}

def addEstoque():
    os.system('cls')
    nome_produto = str(input("Insira o nome do produto que gostaria de adicionar: "))
    try:
        quantidade_produto = int(input("Insira a quantidade do produto a ser adicionada como um numero inteiro: "))
        if quantidade_produto < 0:
            print("Input invalido. Tente novamente.")
            input("Pressione enter para continuar...")
            menu()
        else:    
            estoque[nome_produto] = quantidade_produto
            print("Produto adicionado ao estoque.")
            input("\nPressione enter para continuar...")
            menu()
    except:
        print("Input invalido. Tente novamente.")
        input("Pressione enter para continuar...")
        menu()

def atualizarEstoque():
    os.system('cls')
    nome_produto = str(input("Insira o nome do produto que gostaria de atualizar o estoque: "))
    if nome_produto in estoque:
        try:
            quantidade_produto = int(input("Insira para qual valor a quantidade do produto deveria ser atualizada (numero inteiro): "))
            if quantidade_produto < 0:
                print("Input invalido. Tente novamente.")
                input("Pressione enter para continuar...")
                menu()
            else:    
            estoque[nome_produto] = quantidade_produto
                print("Produto adicionado ao estoque.")
                input("\nPressione enter para continuar...")
                menu()
        except:
            print("Input invalido. Tente novamente.")
            input("Pressione enter para continuar...")
            menu()
    else:
        print("Produto inserido não encontrado no estoque. Tente novamente.")
        input("Aperte enter para continuar...")
        menu()

def exibirEstoque():
    os.system('cls')
    for produtos in estoque:
        print(f"Produto: {produtos}. Quantidade: {estoque[produtos]}.")
    input("\nAperte enter para continuar...")
    menu()


def menu():
    os.system('cls')
    print("Menu:\n1. Adicionar conteudo ao estoque\n2. Atualizar quantidade de um produto do estoque\n3. Exibir estoque\n4. Sair")
    escolha = input("Escolha oque quer fazer: ")
    if escolha == "1":
        addEstoque()
    elif escolha == "2":
        atualizarEstoque()
    elif escolha == "3":
        exibirEstoque()
    elif escolha == "4":
        os.system('cls')
        print("Finalizando app...")
        input("\nPressione enter para continuar...")
        os.system('cls')
    else:
        print("Input invalido. Tente novamente")
        input("Aperte enter para continuar...")
        menu()

menu()

#O programa funciona a partir de varias funcoes, iniciando pelo Menu, onde o usuario é apresentado por uma lista de opções e pedido por um input. Se o input corresponder a uma das opções dadas, a funcção correspondente ao numero da lista escolhido será executada. Caso contrario ele dara um erro ao usuario e executara a função do Menu novamente, re-iniciando o programa para o usuario poder tentar novamente.
#Na primeira opção, uma função de adicionar produtos ao estoque é inicianda onde o usuario é requisitado para inserir um nome para o produto e uma quantidade como numero inteiro positivo. O nome é inserida como chave e a quantidade como valor no dicionario 'estoque'. Caso a quantidade inserida não seja um numero inteiro, ele informa o usuario que o input é invalido e o retorna para o menu.
#Na segunda opção o usuario inicia a função para atualizar a quantidade de um produto, assim ele é requisitade pelo nome do produto que quer adiconar, caso o produto esteja na lista ele é requisitado por um numero inteiro para atualizar a quantidade do produto. Caso o produto não esteja listado no estoque ou o valor da quantiade não for um numero inteiro positivo, o usuario é retornado ao menu.
#Na terceira opção, uma função é iniciado onde ele mostra ao usuario todos os protudos no estoque e suas quantidades.  E depois retorna o usuario ao menu.
#Na quarta opção o programa encerra.