# -----------------------------------------
# Project 22: Student Management System
# Author: Saifullah Haidari
# -----------------------------------------

students = []

while True:
    print("\n" + "=" * 50)
    print("      STUDENT MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter student name: ")
        students.append(name)
        print(f"{name} added successfully.")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            print("\nStudent List:")
            for i, student in enumerate(students, start=1):
                print(f"{i}. {student}")

    elif choice == "3":
        name = input("Enter student name to search: ")

        if name in students:
            print(f"{name} was found.")
        else:
            print(f"{name} was not found.")

    elif choice == "4":
        name = input("Enter student name to remove: ")

        if name in students:
            students.remove(name)
            print(f"{name} removed successfully.")
        else:
            print("Student not found.")

    elif choice == "5":
        print("Exiting Student Management System...")
        break

    else:
        print("Invalid choice. Please try again.")



==================================================
      STUDENT MANAGEMENT SYSTEM
==================================================
1. Add Student
2. View Students
3. Search Student
4. Remove Student
5. Exit

Enter your choice (1-5): 1
Enter student name: Saifullah
Saifullah added successfully.

Enter your choice (1-5): 1
Enter student name: Ahmad
Ahmad added successfully.

Enter your choice (1-5): 2

Student List:
1. Saifullah
2. Ahmad

Enter your choice (1-5): 3
Enter student name to search: Ahmad
Ahmad was found.

Enter your choice (1-5): 4
Enter student name to remove: Ahmad
Ahmad removed successfully.

Enter your choice (1-5): 2

Student List:
1. Saifullah

Enter your choice (1-5): 5
Exiting Student Management System...
