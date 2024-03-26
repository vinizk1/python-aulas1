def mostrar_lista(lista):
    print("Lista:", lista)

def adicionar_item(lista):
    adicionar_item = input("Digite um item novo: ")
    lista.append(adicionar_item)
    mostrar_lista(lista)

def excluir_item(lista):
    excluir = input("Digite o item a ser excluído: ")
    if excluir in lista:
        lista.remove(excluir)
        print(" O item foi removido :)")
    else:
        print("O item não existe :/ ")
    mostrar_lista(lista)

def main():
    lista = []
    while True:
        print("\n--- Menu ---")
        print("1. Inserir um novo item")
        print("2. Excluir um item")
        print("3. Mostrar lista atual")
        print("4. Sair")

        n = input("Escolha uma opção: ")

        if n == "1":
            adicionar_item(lista)
        elif n == "2":
            excluir_item(lista)
        elif n == "3":
            mostrar_lista(lista)
        elif n == "4":
            print("Bye bye!")
            break
        else:
            print("Opção inválida >:( ")

if __name__ == "__main__":
    main()
