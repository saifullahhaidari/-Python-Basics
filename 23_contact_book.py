# -----------------------------------------
# Project 23: Contact Book
# Author: Saifullah Haidari
# -----------------------------------------

contacts = {}

while True:
    print("\n" + "=" * 50)
    print("             CONTACT BOOK")
    print("=" * 50)
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print(f"{name} added successfully.")

    elif choice == "2":
        if not contacts:
            print("No contacts available.")
        else:
            print("\nContact List")
            print("-" * 30)
            for name, phone in contacts.items():
                print(f"{name}: {phone}")

    elif choice == "3":
        name = input("Enter contact name: ")

        if name in contacts:
            print(f"{name}'s phone number is {contacts[name]}")
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter contact name to delete: ")

        if name in contacts:
            del contacts[name]
            print(f"{name} deleted successfully.")
        else:
            print("Contact not found.")

    elif choice == "5":
        print("Thank you for using Contact Book.")
        break

    else:
        print("Invalid choice. Please try again.")



==================================================
             CONTACT BOOK
==================================================
1. Add Contact
2. View Contacts
3. Search Contact
4. Delete Contact
5. Exit

Enter your choice (1-5): 1
Enter contact name: Ali
Enter phone number: 08123456789
Ali added successfully.

Enter your choice (1-5): 1
Enter contact name: Sara
Enter phone number: 08987654321
Sara added successfully.

Enter your choice (1-5): 2

Contact List
------------------------------
Ali: 08123456789
Sara: 08987654321

Enter your choice (1-5): 3
Enter contact name: Sara
Sara's phone number is 08987654321

Enter your choice (1-5): 4
Enter contact name to delete: Ali
Ali deleted successfully.

Enter your choice (1-5): 5
Thank you for using Contact Book.
