# -----------------------------------------
# Project 09: Student Grade Calculator
# Author: Saifullah Haidari
# -----------------------------------------

print("=" * 50)
print("        STUDENT GRADE CALCULATOR")
print("=" * 50)

# Get student information
name = input("Enter student's name: ")
score = float(input("Enter student's score (0 - 100): "))

# Validate score
if score < 0 or score > 100:
    print("\nInvalid score! Please enter a value between 0 and 100.")

else:
    # Calculate grade
    if score >= 90:
        grade = "A"
        status = "Excellent"

    elif score >= 80:
        grade = "B"
        status = "Very Good"

    elif score >= 70:
        grade = "C"
        status = "Good"

    elif score >= 60:
        grade = "D"
        status = "Pass"

    else:
        grade = "F"
        status = "Fail"

    print("\n" + "=" * 50)
    print("Student Report")
    print("=" * 50)
    print(f"Name   : {name}")
    print(f"Score  : {score:.1f}")
    print(f"Grade  : {grade}")
    print(f"Status : {status}")
    print("=" * 50)

print("\nThank you for using Student Grade Calculator!")


==================================================
        STUDENT GRADE CALCULATOR
==================================================
Enter student's name: Saifullah
Enter student's score (0 - 100): 88

==================================================
Student Report
==================================================
Name   : Saifullah
Score  : 88.0
Grade  : B
Status : Very Good
==================================================

Thank you for using Student Grade Calculator!
