# -----------------------------------------
# Project 18: Unit Converter
# Author: Saifullah Haidari
# -----------------------------------------

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462


print("=" * 50)
print("            UNIT CONVERTER")
print("=" * 50)

print("1. Kilometers → Miles")
print("2. Miles → Kilometers")
print("3. Kilograms → Pounds")
print("4. Pounds → Kilograms")

choice = input("\nEnter your choice (1-4): ")

value = float(input("Enter the value: "))

if choice == "1":
    print(f"\nResult: {km_to_miles(value):.2f} miles")

elif choice == "2":
    print(f"\nResult: {miles_to_km(value):.2f} km")

elif choice == "3":
    print(f"\nResult: {kg_to_pounds(value):.2f} lb")

elif choice == "4":
    print(f"\nResult: {pounds_to_kg(value):.2f} kg")

else:
    print("\nInvalid choice!")

print("\nThank you for using Unit Converter.")


==================================================
            UNIT CONVERTER
==================================================
1. Kilometers → Miles
2. Miles → Kilometers
3. Kilograms → Pounds
4. Pounds → Kilograms

Enter your choice (1-4): 3
Enter the value: 10

Result: 22.05 lb

Thank you for using Unit Converter.
