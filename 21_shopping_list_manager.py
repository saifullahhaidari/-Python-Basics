# -----------------------------------------
# Project 21: Shopping List Manager
# Author: Saifullah Haidari
# -----------------------------------------

shopping_list = []

while True:
    print("\n" + "=" * 50)
    print("         SHOPPING LIST MANAGER")
    print("=" * 50)
    print("1. Add Item")
    print("2. View List")
    print("3. Remove Item")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        item = input("Enter item name: ")
        shopping_list.append(item)
        print(f"{item} added successfully.")

    elif choice == "2":
        if len(shopping_list) == 0:
            print("Shopping list is empty.")
        else:
            print("\nShopping List:")
            for i, item in enumerate(shopping_list, start=1):
                print(f"{i}. {item}")

    elif choice == "3":
        item = input("Enter item to remove: ")

        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed successfully.")
        else:
            print("Item not found.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")



==================================================
         SHOPPING LIST MANAGER
==================================================
1. Add Item
2. View List
3. Remove Item
4. Exit

Enter your choice (1-4): 1
Enter item name: Milk
Milk added successfully.

Enter your choice (1-4): 1
Enter item name: Bread
Bread added successfully.

Enter your choice (1-4): 2

Shopping List:
1. Milk
2. Bread

Enter your choice (1-4): 3
Enter item to remove: Milk
Milk removed successfully.

Enter your choice (1-4): 2

Shopping List:
1. Bread

Enter your choice (1-4): 4
Goodbye!
