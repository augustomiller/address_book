

def add_new_contact(contacts, new_contact, cellphone_number, email):
    contact_info = {"contact": new_contact, "cellphone": cellphone_number, "email": email, "favorite": False}
    contacts.append(contact_info)
    print(f"\n Contato {new_contact} , {cellphone_number} , {email} foi adicionado com sucesso! ✅")
    # print(contacts)
    return

def view_contact(contacts):
    print("Lista de contatos:")
    for i, contact in enumerate(contacts, start=1):
        favorite_status = "⁜" if contact["favorite"] else " "
        contact_name = contact["contact"]
        print(f"\n {i}.[{favorite_status}] {contact_name}, {cellphone_number}, {email}.")
    return

contacts = []
while True:
    print("\n Agenda de Contatos")
    print("1 - Adicionar contato")
    print("2 - Visualizar a lista de contatos")
    print("3 - Editar contato")
    print("4 - Marcar contato como favorito")
    print("5 - Desmarcar favorito")
    print("6 - Visualizar lista de favoritos")
    print("7 - Deletar contato")
    print("8 - Sair do programa")

    choice = input("\n Digite sua escolha: ")

    if choice == "1":
        new_contact = input("Digite o nome do contato Āβ: ")
        cellphone_number = input("Digite o número do contato 📱: ")
        email = input("Digite o email do contato ✉️: ")
        add_new_contact(contacts, new_contact, cellphone_number, email)

    elif choice == "2":
        view_contact(contacts)

    elif choice == "3":
        print("Choice 3 selected!")

    elif choice == "4":
        print("Choice 4 selected!")

    elif choice == "5":
        print("Choice 5 selected!")

    elif choice == "6":
        print("Choice 6 selected!")

    elif choice == "7":
        print("Choice 4 selected!")

    elif choice == "8":
        break

print("\n Você saiu da agenda 😞")