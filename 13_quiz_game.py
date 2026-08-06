# -----------------------------------------
# Project 13: Quiz Game
# Author: Saifullah Haidari
# -----------------------------------------

print("=" * 50)
print("              QUIZ GAME")
print("=" * 50)

score = 0

# Question 1
print("\n1. What is the capital of Indonesia?")
print("A. Jakarta")
print("B. Surabaya")
print("C. Bali")
answer = input("Your answer: ").upper()

if answer == "A":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is A.")

# Question 2
print("\n2. Which language is mainly used for AI and Machine Learning?")
print("A. Java")
print("B. Python")
print("C. HTML")
answer = input("Your answer: ").upper()

if answer == "B":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is B.")

# Question 3
print("\n3. How many days are there in a leap year?")
print("A. 364")
print("B. 365")
print("C. 366")
answer = input("Your answer: ").upper()

if answer == "C":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is C.")

# Final Result
print("\n" + "=" * 50)
print("Quiz Result")
print("=" * 50)
print(f"Your Score: {score}/3")

if score == 3:
    print("Excellent!")
elif score == 2:
    print("Very Good!")
elif score == 1:
    print("Good! Keep practicing.")
else:
    print("Better luck next time!")

print("=" * 50)
print("Thank you for playing!")


==================================================
              QUIZ GAME
==================================================

1. What is the capital of Indonesia?
A. Jakarta
B. Surabaya
C. Bali
Your answer: A
Correct!

2. Which language is mainly used for AI and Machine Learning?
A. Java
B. Python
C. HTML
Your answer: B
Correct!

3. How many days are there in a leap year?
A. 364
B. 365
C. 366
Your answer: C
Correct!

==================================================
Quiz Result
==================================================
Your Score: 3/3
Excellent!
==================================================
Thank you for playing!
