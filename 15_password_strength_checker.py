# -----------------------------------------
# Project 15: Password Strength Checker
# Author: Saifullah Haidari
# -----------------------------------------

print("=" * 50)
print("      PASSWORD STRENGTH CHECKER")
print("=" * 50)

password = input("Enter your password: ")

has_upper = False
has_lower = False
has_digit = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True

print("\n" + "=" * 50)

if len(password) < 8:
    print("Weak Password")
elif has_upper and has_lower and has_digit:
    print("Strong Password")
else:
    print("Medium Password")

print("=" * 50)


==================================================
      PASSWORD STRENGTH CHECKER
==================================================
Enter your password: abc123

==================================================
Weak Password
==================================================


  ==================================================
      PASSWORD STRENGTH CHECKER
==================================================
Enter your password: Password123

==================================================
Strong Password
==================================================


  
