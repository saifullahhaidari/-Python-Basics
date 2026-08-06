# -----------------------------------------
# Project 11: Multiplication Table
# Author: Saifullah Haidari
# -----------------------------------------

print("=" * 50)
print("        MULTIPLICATION TABLE")
print("=" * 50)

number = int(input("Enter a number: "))

print(f"\nMultiplication Table of {number}\n")

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

print("\nDone!")

==================================================
        MULTIPLICATION TABLE
==================================================
Enter a number: 7

Multiplication Table of 7

7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70

Done!
