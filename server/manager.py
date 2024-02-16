

def add_new_contact(contacts, new_contact, cellphone_number, email):
    contact_info = {"contact": new_contact, "cellphone": cellphone_number, "email": email, "favorite": False}
    contacts.append(contact_info)
    print(f"\n Contato {new_contact} , {cellphone_number} , {email} foi adicionado com sucesso! ✅")
    return

def view_contact(contacts):
    print("\n Lista de contatos:")

    for i, contact in enumerate(contacts, start=1):
        print(contacts)
        favorite_status = "⁜" if contact["favorite"] else " "
        contact_name = contact["contact"]
        cellphone_number = contact["cellphone"]
        email = contact["email"]

        print(f"\n {i}.[{favorite_status}] {contact_name}, {cellphone_number}, {email}.")
    return

def edit_contact(contacts, index_contact, new_contact_edited, cellphone_number_edited, email_edited):
    adjusted_contact_index = int(index_contact) -1

    if adjusted_contact_index >= 0 and adjusted_contact_index < len(contacts):
        contacts[adjusted_contact_index]["contact"] = new_contact_edited
        contacts[adjusted_contact_index]["cellphone"] = cellphone_number_edited
        contacts[adjusted_contact_index]["email"] = email_edited

        print(f"\n Tarefa {index_contact} atualizada para {new_contact_edited}, {cellphone_number_edited}, {email_edited}")
    else:
        print("\n Índice de tarefa inválido!")
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
        email = input("Digite o email do contato 📩: ")
        add_new_contact(contacts, new_contact, cellphone_number, email)

    elif choice == "2":
        view_contact(contacts)

    elif choice == "3":
        view_contact(contacts)
        index_contact = input("Digite o número do contato que gostaria editar: ")
        new_contact_edited = input("Digite o nome do contato Āβ: ")
        cellphone_number_edited = input("Digite o número do contato 📱: ")
        email_edited = input("Digite o email do contato 📩: ")

        edit_contact(contacts, index_contact, new_contact_edited, cellphone_number_edited, email_edited)

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