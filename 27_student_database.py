# -----------------------------------------
# Project 27: Student Database
# Author: Saifullah Haidari
# -----------------------------------------

FILE_NAME = "students.txt"

while True:
    print("\n" + "=" * 50)
    print("           STUDENT DATABASE")
    print("=" * 50)
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        name = input("Enter student name: ")
        age = input("Enter age: ")
        department = input("Enter department: ")

        with open(FILE_NAME, "a") as file:
            file.write(f"{name}, {age}, {department}\n")

        print("Student saved successfully.")

    elif choice == "2":
        try:
            with open(FILE_NAME, "r") as file:
                students = file.readlines()

            if len(students) == 0:
                print("No student records found.")
            else:
                print("\nStudent Records")
                print("-" * 50)

                for i, student in enumerate(students, start=1):
                    print(f"{i}. {student.strip()}")

        except FileNotFoundError:
            print("Database file not found.")

    elif choice == "3":
        print("Thank you for using Student Database.")
        break

    else:
        print("Invalid choice. Please try again.")

  ==================================================
           STUDENT DATABASE
==================================================
1. Add Student
2. View Students
3. Exit

Enter your choice (1-3): 1

Enter student name: Saifullah
Enter age: 29
Enter department: Computer Engineering

Student saved successfully.

==================================================
           STUDENT DATABASE
==================================================
1. Add Student
2. View Students
3. Exit

Enter your choice (1-3): 2

Student Records
--------------------------------------------------
1. Saifullah, 29, Computer Engineering

==================================================
           STUDENT DATABASE
==================================================
1. Add Student
2. View Students
3. Exit

Enter your choice (1-3): 3

Thank you for using Student Database.
