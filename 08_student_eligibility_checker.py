# -----------------------------------------
# Project 08: Student Eligibility Checker
# Author: Saifullah Haidari
# -----------------------------------------

print("=" * 50)
print("      STUDENT ELIGIBILITY CHECKER")
print("=" * 50)

# Get student information
name = input("Enter student's name: ")
age = int(input("Enter student's age: "))
gpa = float(input("Enter student's GPA (0.0 - 4.0): "))

print("\nChecking eligibility...\n")

# Check eligibility
if age >= 18 and gpa >= 3.0:
    status = "Eligible"
    message = "Congratulations! You meet all admission requirements."

elif age >= 18 and gpa < 3.0:
    status = "Not Eligible"
    message = "Your GPA is below the minimum requirement."

elif age < 18 and gpa >= 3.0:
    status = "Not Eligible"
    message = "You do not meet the minimum age requirement."

else:
    status = "Not Eligible"
    message = "You do not meet both age and GPA requirements."

# Display result
print("=" * 50)
print("Eligibility Report")
print("=" * 50)
print(f"Student Name : {name}")
print(f"Age          : {age}")
print(f"GPA          : {gpa:.2f}")
print(f"Status       : {status}")
print(f"Message      : {message}")
print("=" * 50)

print("\nThank you for using Student Eligibility Checker!")

==================================================
      STUDENT ELIGIBILITY CHECKER
==================================================
Enter student's name: Saifullah
Enter student's age: 24
Enter student's GPA (0.0 - 4.0): 3.7

Checking eligibility...

==================================================
Eligibility Report
==================================================
Student Name : Saifullah
Age          : 24
GPA          : 3.70
Status       : Eligible
Message      : Congratulations! You meet all admission requirements.
==================================================

Thank you for using Student Eligibility Checker!

