#Contact Management System

contacts = []


def is_valid_phone(phone):
    #Return True if phone is exactly 10 digits, else False.
    return len(phone) == 10 and phone.isdigit()


def phone_exists(phone):
    #Return True if this phone number is already in the list.
    for contact in contacts:
        if contact["phone"] == phone:
            return True
    return False


def add_contact():
    #Create: add a new contact.
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()

    if not is_valid_phone(phone):
        print("Invalid phone number. Enter exactly 10 digits.")
        return

    if phone_exists(phone):
        print("Contact with this number already exists.")
        return

    email = input("Enter email: ").strip()
    contacts.append({"name": name, "phone": phone, "email": email})
    print(f"Contact added: {name} | {phone}")


def view_contacts():
    #Read: show all contacts.
    if not contacts:
        print("No contacts found.")
        return

    for contact in contacts:
        print(f"{contact['name']} | {contact['phone']} | {contact['email']}")


def search_contact():
    #Read: search a contact by name.
    keyword = input("Enter name to search: ").strip().lower()

    for contact in contacts:
        if keyword in contact["name"].lower():
            print(f"{contact['name']} | {contact['phone']} | {contact['email']}")
            return

    print("Contact not found.")


def update_contact():
    #Update: change the phone number of a contact.
    name = input("Enter name to update: ").strip()

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            new_phone = input("Enter new phone number: ").strip()

            if not is_valid_phone(new_phone):
                print("Invalid phone number. Enter exactly 10 digits.")
                return

            if new_phone != contact["phone"] and phone_exists(new_phone):
                print("Contact with this number already exists.")
                return

            contact["phone"] = new_phone
            print(f"Phone updated: {new_phone}")
            return

    print("Contact not found.")


def delete_contact():
    #Delete: remove a contact by name.
    name = input("Enter name to delete: ").strip()

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print(f"Contact '{contact['name']}' deleted. Total contacts: {len(contacts)}")
            return

    print("Contact not found.")


def main():
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
