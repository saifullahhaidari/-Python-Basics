# -----------------------------------------
# Project 14: ATM Menu
# Author: Saifullah Haidari
# -----------------------------------------

balance = 1000

while True:
    print("\n" + "=" * 50)
    print("               ATM MENU")
    print("=" * 50)
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        print(f"\nYour current balance is: ${balance}")

    elif choice == "2":
        deposit = float(input("Enter deposit amount: $"))
        balance += deposit
        print(f"Deposit successful! New balance: ${balance}")

    elif choice == "3":
        withdraw = float(input("Enter withdrawal amount: $"))

        if withdraw <= balance:
            balance -= withdraw
            print(f"Withdrawal successful! New balance: ${balance}")
        else:
            print("Insufficient balance!")

    elif choice == "4":
        print("\nThank you for using our ATM!")
        break

    else:
        print("Invalid choice. Please try again.")


==================================================
               ATM MENU
==================================================
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit

Enter your choice (1-4): 1

Your current balance is: $1000

==================================================
               ATM MENU
==================================================
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit

Enter your choice (1-4): 2
Enter deposit amount: $500

Deposit successful! New balance: $1500

==================================================
               ATM MENU
==================================================
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit

Enter your choice (1-4): 3
Enter withdrawal amount: $300

Withdrawal successful! New balance: $1200

==================================================
               ATM MENU
==================================================
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit

Enter your choice (1-4): 4

Thank you for using our ATM!
