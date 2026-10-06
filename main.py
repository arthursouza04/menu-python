def mostrar_menu():
    print("=== Menu ===")
    print("1 - Ver mensagem")
    print("0 - Sair")


def mostrar_mensagem():
    print("Bem-vindo!")


mostrar_menu()


opcao = input("Escolha: ")


if opcao == "1":
    mostrar_mensagem()
elif opcao == "0":
    print("Encerrando...")
else:
    print("Opção inválida!")

