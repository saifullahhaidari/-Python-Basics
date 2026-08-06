# -----------------------------------------
# Project 10: BMI Calculator
# Author: Saifullah Haidari
# -----------------------------------------

print("=" * 50)
print("            BMI CALCULATOR")
print("=" * 50)

name = input("Enter your name: ")
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print("\n" + "=" * 50)
print("BMI Report")
print("=" * 50)
print(f"Name     : {name}")
print(f"Weight   : {weight:.1f} kg")
print(f"Height   : {height:.2f} m")
print(f"BMI      : {bmi:.2f}")
print(f"Category : {category}")
print("=" * 50)

print("\nThank you for using BMI Calculator!")

==================================================
            BMI CALCULATOR
==================================================
Enter your name: Saifullah
Enter your weight (kg): 72
Enter your height (m): 1.75

==================================================
BMI Report
==================================================
Name     : Saifullah
Weight   : 72.0 kg
Height   : 1.75 m
BMI      : 23.51
Category : Normal
==================================================

Thank you for using BMI Calculator!
