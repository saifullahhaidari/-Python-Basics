# -----------------------------------------
# Project 30: Employee Management System
# Author: Saifullah Haidari
# -----------------------------------------

class Employee:

    def __init__(self, emp_id, name, position, salary):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary


class EmployeeManager:

    def __init__(self):
        self.employees = []

    def add_employee(self):
        emp_id = input("Employee ID: ")
        name = input("Name: ")
        position = input("Position: ")
        salary = float(input("Salary: "))

        employee = Employee(emp_id, name, position, salary)
        self.employees.append(employee)

        print("Employee added successfully.")

    def show_employees(self):
        if not self.employees:
            print("No employees found.")
        else:
            print("\nEmployee List")
            print("-" * 60)

            for emp in self.employees:
                print(f"ID: {emp.emp_id}")
                print(f"Name: {emp.name}")
                print(f"Position: {emp.position}")
                print(f"Salary: ${emp.salary:.2f}")
                print("-" * 60)

    def search_employee(self):
        emp_id = input("Enter Employee ID: ")

        for emp in self.employees:
            if emp.emp_id == emp_id:
                print("\nEmployee Found")
                print(f"ID: {emp.emp_id}")
                print(f"Name: {emp.name}")
                print(f"Position: {emp.position}")
                print(f"Salary: ${emp.salary:.2f}")
                return

        print("Employee not found.")


manager = EmployeeManager()

while True:

    print("\n" + "=" * 50)
    print("     EMPLOYEE MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add Employee")
    print("2. Show Employees")
    print("3. Search Employee")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        manager.add_employee()

    elif choice == "2":
        manager.show_employees()

    elif choice == "3":
        manager.search_employee()

    elif choice == "4":
        print("Thank you for using Employee Management System.")
        break

    else:
        print("Invalid choice.")


==================================================
     EMPLOYEE MANAGEMENT SYSTEM
==================================================
1. Add Employee
2. Show Employees
3. Search Employee
4. Exit

Enter your choice (1-4): 1

Employee ID: 101
Name: Saifullah Haidari
Position: AI Researcher
Salary: 5000

Employee added successfully.

==================================================
Enter your choice (1-4): 2

Employee List
------------------------------------------------------------
ID: 101
Name: Saifullah Haidari
Position: AI Researcher
Salary: $5000.00
------------------------------------------------------------

==================================================
Enter your choice (1-4): 3

Enter Employee ID: 101

Employee Found
ID: 101
Name: Saifullah Haidari
Position: AI Researcher
Salary: $5000.00

==================================================
Enter your choice (1-4): 4

Thank you for using Employee Management System.
