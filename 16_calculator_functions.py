# -----------------------------------------
# Project 16: Calculator Using Functions
# Author: Saifullah Haidari
# -----------------------------------------

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b


print("=" * 50)
print("      CALCULATOR USING FUNCTIONS")
print("=" * 50)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nSelect Operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("\nEnter your choice (1-4): ")

if choice == "1":
    print(f"\nResult = {add(num1, num2)}")

elif choice == "2":
    print(f"\nResult = {subtract(num1, num2)}")

elif choice == "3":
    print(f"\nResult = {multiply(num1, num2)}")

elif choice == "4":
    print(f"\nResult = {divide(num1, num2)}")

else:
    print("\nInvalid choice!")

print("\nThank you for using the calculator.")


==================================================
      CALCULATOR USING FUNCTIONS
==================================================
Enter first number: 25
Enter second number: 5

Select Operation
1. Addition
2. Subtraction
3. Multiplication
4. Division

Enter your choice (1-4): 4

Result = 5.0

Thank you for using the calculator.


