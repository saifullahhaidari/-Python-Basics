"""
Project 04: Type Conversion
Author: Saifullah Haidari

Description:
This program demonstrates how to convert
between different Python data types.
"""

# String to Integer
age = "25"
new_age = int(age)

# Integer to Float
score = 95
new_score = float(score)

# Float to String
gpa = 3.85
new_gpa = str(gpa)

# Integer to Boolean
number = 1
new_boolean = bool(number)

print("===== Type Conversion =====")

print(new_age, type(new_age))
print(new_score, type(new_score))
print(new_gpa, type(new_gpa))
print(new_boolean, type(new_boolean))
نتیجه 
===== Type Conversion =====

25 <class 'int'>

95.0 <class 'float'>

3.85 <class 'str'>

True <class 'bool'>
