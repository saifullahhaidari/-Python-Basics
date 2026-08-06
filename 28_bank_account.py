# -----------------------------------------
# Project 28: Bank Account System
# Author: Saifullah Haidari
# -----------------------------------------

class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount:.2f}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: ${amount:.2f}")
        else:
            print("Insufficient balance.")

    def show_balance(self):
        print(f"Owner   : {self.owner}")
        print(f"Balance : ${self.balance:.2f}")


owner = input("Enter account owner: ")
account = BankAccount(owner)

while True:
    print("\n" + "=" * 50)
    print("          BANK ACCOUNT SYSTEM")
    print("=" * 50)
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter amount: "))
        account.withdraw(amount)

    elif choice == "3":
        account.show_balance()

    elif choice == "4":
        print("Thank you for using Bank Account System.")
        break

    else:
        print("Invalid choice.")

  Enter account owner: Saifullah

==================================================
          BANK ACCOUNT SYSTEM
==================================================
1. Deposit
2. Withdraw
3. Show Balance
4. Exit

Enter your choice (1-4): 1
Enter amount: 1000
Deposited: $1000.00

==================================================
          BANK ACCOUNT SYSTEM
==================================================
1. Deposit
2. Withdraw
3. Show Balance
4. Exit

Enter your choice (1-4): 2
Enter amount: 250
Withdrawn: $250.00

==================================================
          BANK ACCOUNT SYSTEM
==================================================
1. Deposit
2. Withdraw
3. Show Balance
4. Exit

Enter your choice (1-4): 3
Owner   : Saifullah
Balance : $750.00

==================================================
          BANK ACCOUNT SYSTEM
==================================================
1. Deposit
2. Withdraw
3. Show Balance
4. Exit

Enter your choice (1-4): 4

Thank you for using Bank Account System.
