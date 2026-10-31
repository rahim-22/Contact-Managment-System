contacts = []

def valid_phone(phone):
    return phone.isdigit() and len(phone) == 10

def phone_exists(phone, current_contact=None):
    for contact in contacts:
        if contact["phone"] == phone and contact is not current_contact:
            return True
    return False

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()

    if not valid_phone(phone):
        print("Invalid phone number. Enter exactly 10 digits.")
        return

    if phone_exists(phone):
        print("Contact with this number already exists.")
        return

    contacts.append({"name": name, "phone": phone, "email": email})
    print(f"Contact added: {name} | {phone}")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return

    for contact in contacts:
        print(f'{contact["name"]} | {contact["phone"]} | {contact["email"]}')

def search_contact():
    name = input("Enter name to search: ").strip()

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print(f'{contact["name"]} | {contact["phone"]} | {contact["email"]}')
            return

    print("Contact not found.")

def update_contact():
    name = input("Enter name to update: ").strip()

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            new_phone = input("Enter new phone: ").strip()

            if not valid_phone(new_phone):
                print("Invalid phone number. Enter exactly 10 digits.")
                return

            if phone_exists(new_phone, contact):
                print("Contact with this number already exists.")
                return

            contact["phone"] = new_phone
            print(f"Phone updated: {new_phone}")
            return

    print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ").strip()

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print(f"Contact '{contact['name']}' deleted. Total contacts: {len(contacts)}")
            return

    print("Contact not found.")

def menu():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter option: ").strip()

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
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    menu()
