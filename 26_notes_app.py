# -----------------------------------------
# Project 26: Notes App
# Author: Saifullah Haidari
# -----------------------------------------

FILE_NAME = "notes.txt"

while True:
    print("\n" + "=" * 50)
    print("               NOTES APP")
    print("=" * 50)
    print("1. Add Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        note = input("Write your note: ")

        with open(FILE_NAME, "a") as file:
            file.write(note + "\n")

        print("Note saved successfully.")

    elif choice == "2":
        try:
            with open(FILE_NAME, "r") as file:
                notes = file.readlines()

            if len(notes) == 0:
                print("No notes available.")
            else:
                print("\nYour Notes")
                print("-" * 50)

                for i, note in enumerate(notes, start=1):
                    print(f"{i}. {note.strip()}")

        except FileNotFoundError:
            print("No notes file found.")

    elif choice == "3":
        print("Thank you for using Notes App.")
        break

    else:
        print("Invalid choice. Please try again.")


==================================================
               NOTES APP
==================================================
1. Add Note
2. View Notes
3. Exit

Enter your choice (1-3): 1

Write your note:
Learn Python Functions

Note saved successfully.

==================================================
               NOTES APP
==================================================
1. Add Note
2. View Notes
3. Exit

Enter your choice (1-3): 1

Write your note:
Finish GitHub Projects

Note saved successfully.

==================================================
               NOTES APP
==================================================
1. Add Note
2. View Notes
3. Exit

Enter your choice (1-3): 2

Your Notes
--------------------------------------------------
1. Learn Python Functions
2. Finish GitHub Projects

==================================================
               NOTES APP
==================================================
1. Add Note
2. View Notes
3. Exit

Enter your choice (1-3): 3

Thank you for using Notes App.
