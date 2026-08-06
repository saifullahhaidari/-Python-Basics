# -----------------------------------------
# Project 19: Password Generator
# Author: Saifullah Haidari
# -----------------------------------------

import random
import string

print("=" * 50)
print("         PASSWORD GENERATOR")
print("=" * 50)

length = int(input("Enter password length: "))

characters = (
    string.ascii_letters +
    string.digits +
    string.punctuation
)

password = ""

for i in range(length):
    password += random.choice(characters)

print("\n" + "=" * 50)
print("Generated Password")
print("=" * 50)
print(password)
print("=" * 50)

print("\nPassword generated successfully!")


==================================================
         PASSWORD GENERATOR
==================================================
Enter password length: 12

==================================================
Generated Password
==================================================
A#7kP@9x!Q2$
==================================================

Password generated successfully!
