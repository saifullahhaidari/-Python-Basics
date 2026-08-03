"""
Project 02: Interactive Personal Profile
Author: Saifullah Haidari

Description:
This program collects personal information from the user
and displays it in a formatted profile.
"""

print("===== Personal Profile =====")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
country = input("Enter your country: ")
university = input("Enter your university: ")

print("\n===== Your Profile =====")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Country: {country}")
print(f"University: {university}")
