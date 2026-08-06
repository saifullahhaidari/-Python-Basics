# -----------------------------------------
# Project 20: Student Result System
# Author: Saifullah Haidari
# -----------------------------------------

def calculate_average(scores):
    return sum(scores) / len(scores)


def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


print("=" * 50)
print("        STUDENT RESULT SYSTEM")
print("=" * 50)

name = input("Enter student name: ")

scores = []

for i in range(3):
    score = float(input(f"Enter score {i + 1}: "))
    scores.append(score)

average = calculate_average(scores)
grade = get_grade(average)

print("\n" + "=" * 50)
print("Student Report")
print("=" * 50)
print(f"Name    : {name}")
print(f"Scores  : {scores}")
print(f"Average : {average:.2f}")
print(f"Grade   : {grade}")
print("=" * 50)




==================================================
        STUDENT RESULT SYSTEM
==================================================
Enter student name: Saifullah
Enter score 1: 90
Enter score 2: 85
Enter score 3: 95

==================================================
Student Report
==================================================
Name    : Saifullah
Scores  : [90.0, 85.0, 95.0]
Average : 90.00
Grade   : A
==================================================
