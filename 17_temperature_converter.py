# -----------------------------------------
# Project 17: Temperature Converter
# Author: Saifullah Haidari
# -----------------------------------------

def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15


print("=" * 50)
print("        TEMPERATURE CONVERTER")
print("=" * 50)

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")

choice = input("\nChoose an option (1-4): ")

temperature = float(input("Enter temperature: "))

if choice == "1":
    result = celsius_to_fahrenheit(temperature)
    print(f"\nResult: {result:.2f} °F")

elif choice == "2":
    result = fahrenheit_to_celsius(temperature)
    print(f"\nResult: {result:.2f} °C")

elif choice == "3":
    result = celsius_to_kelvin(temperature)
    print(f"\nResult: {result:.2f} K")

elif choice == "4":
    result = kelvin_to_celsius(temperature)
    print(f"\nResult: {result:.2f} °C")

else:
    print("\nInvalid choice!")

print("\nThank you for using Temperature Converter.")


==================================================
        TEMPERATURE CONVERTER
==================================================
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Celsius to Kelvin
4. Kelvin to Celsius

Choose an option (1-4): 1
Enter temperature: 25

Result: 77.00 °F

Thank you for using Temperature Converter.
