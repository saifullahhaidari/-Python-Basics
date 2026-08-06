# -----------------------------------------
# Project 25: Expense Tracker
# Author: Saifullah Haidari
# -----------------------------------------

expenses = []

while True:
    print("\n" + "=" * 50)
    print("           EXPENSE TRACKER")
    print("=" * 50)
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Expense")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        category = input("Enter expense category: ")
        amount = float(input("Enter amount: "))

        expense = {
            "Category": category,
            "Amount": amount
        }

        expenses.append(expense)
        print("Expense added successfully.")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded.")
        else:
            print("\nExpense List")
            print("-" * 50)

            for i, expense in enumerate(expenses, start=1):
                print(f"{i}. {expense['Category']} : ${expense['Amount']:.2f}")

    elif choice == "3":
        total = 0

        for expense in expenses:
            total += expense["Amount"]

        print(f"\nTotal Expense: ${total:.2f}")

    elif choice == "4":
        print("Thank you for using Expense Tracker.")
        break

    else:
        print("Invalid choice. Please try again.")


==================================================
           EXPENSE TRACKER
==================================================
1. Add Expense
2. View Expenses
3. Show Total Expense
4. Exit

Enter your choice (1-4): 1
Enter expense category: Food
Enter amount: 25

Expense added successfully.

Enter your choice (1-4): 1
Enter expense category: Transport
Enter amount: 10

Expense added successfully.

Enter your choice (1-4): 2

Expense List
--------------------------------------------------
1. Food : $25.00
2. Transport : $10.00

Enter your choice (1-4): 3

Total Expense: $35.00

Enter your choice (1-4): 4

Thank you for using Expense Tracker.
