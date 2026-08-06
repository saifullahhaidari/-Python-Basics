# -----------------------------------------
# Project 12: Number Guessing Game
# Author: Saifullah Haidari
# -----------------------------------------

import random

print("=" * 50)
print("        NUMBER GUESSING GAME")
print("=" * 50)

secret_number = random.randint(1, 100)
attempts = 0

print("I have selected a number between 1 and 100.")
print("Can you guess it?\n")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.\n")

    elif guess > secret_number:
        print("Too high! Try again.\n")

    else:
        print("\nCongratulations!")
        print(f"You guessed the correct number: {secret_number}")
        print(f"Total attempts: {attempts}")
        break

print("\nThank you for playing!")

==================================================
        NUMBER GUESSING GAME
==================================================
I have selected a number between 1 and 100.
Can you guess it?

Enter your guess: 50
Too low! Try again.

Enter your guess: 80
Too high! Try again.

Enter your guess: 67

Congratulations!
You guessed the correct number: 67
Total attempts: 3

Thank you for playing!
