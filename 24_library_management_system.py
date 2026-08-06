# -----------------------------------------
# Project 24: Library Management System
# Author: Saifullah Haidari
# -----------------------------------------

library = []

while True:
    print("\n" + "=" * 50)
    print("      LIBRARY MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author name: ")

        book = {
            "Title": title,
            "Author": author
        }

        library.append(book)
        print("Book added successfully.")

    elif choice == "2":
        if len(library) == 0:
            print("No books available.")
        else:
            print("\nLibrary Books")
            print("-" * 50)

            for i, book in enumerate(library, start=1):
                print(f"{i}. {book['Title']} - {book['Author']}")

    elif choice == "3":
        title = input("Enter book title: ")

        found = False

        for book in library:
            if book["Title"].lower() == title.lower():
                print("\nBook Found")
                print(f"Title : {book['Title']}")
                print(f"Author: {book['Author']}")
                found = True
                break

        if not found:
            print("Book not found.")

    elif choice == "4":
        title = input("Enter book title to remove: ")

        found = False

        for book in library:
            if book["Title"].lower() == title.lower():
                library.remove(book)
                print("Book removed successfully.")
                found = True
                break

        if not found:
            print("Book not found.")

    elif choice == "5":
        print("Thank you for using Library Management System.")
        break

    else:
        print("Invalid choice. Please try again.")

  ==================================================
      LIBRARY MANAGEMENT SYSTEM
==================================================
1. Add Book
2. View Books
3. Search Book
4. Remove Book
5. Exit

Enter your choice (1-5): 1
Enter book title: Python Crash Course
Enter author name: Eric Matthes

Book added successfully.

Enter your choice (1-5): 1
Enter book title: Clean Code
Enter author name: Robert C. Martin

Book added successfully.

Enter your choice (1-5): 2

Library Books
--------------------------------------------------
1. Python Crash Course - Eric Matthes
2. Clean Code - Robert C. Martin

Enter your choice (1-5): 3
Enter book title: Clean Code

Book Found
Title : Clean Code
Author: Robert C. Martin

Enter your choice (1-5): 4
Enter book title to remove: Python Crash Course

Book removed successfully.

Enter your choice (1-5): 5

Thank you for using Library Management System.
