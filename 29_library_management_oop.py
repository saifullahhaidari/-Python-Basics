# -----------------------------------------
# Project 29: Library Management System (OOP)
# Author: Saifullah Haidari
# -----------------------------------------

class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print("Book added successfully.")

    def show_books(self):
        if len(self.books) == 0:
            print("No books available.")
        else:
            print("\nLibrary Books")
            print("-" * 40)
            for i, book in enumerate(self.books, start=1):
                print(f"{i}. {book.title} - {book.author}")

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print("Book removed successfully.")
                return

        print("Book not found.")


library = Library()

while True:

    print("\n" + "=" * 50)
    print("      LIBRARY MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add Book")
    print("2. Show Books")
    print("3. Remove Book")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        title = input("Book title: ")
        author = input("Author: ")
        library.add_book(title, author)

    elif choice == "2":
        library.show_books()

    elif choice == "3":
        title = input("Enter book title: ")
        library.remove_book(title)

    elif choice == "4":
        print("Thank you for using Library Management System.")
        break

    else:
        print("Invalid choice.")

  ==================================================
      LIBRARY MANAGEMENT SYSTEM
==================================================
1. Add Book
2. Show Books
3. Remove Book
4. Exit

Enter your choice (1-4): 1

Book title: Python Crash Course
Author: Eric Matthes

Book added successfully.

==================================================
1. Add Book
2. Show Books
3. Remove Book
4. Exit

Enter your choice (1-4): 1

Book title: Clean Code
Author: Robert C. Martin

Book added successfully.

==================================================
1. Add Book
2. Show Books
3. Remove Book
4. Exit

Enter your choice (1-4): 2

Library Books
----------------------------------------
1. Python Crash Course - Eric Matthes
2. Clean Code - Robert C. Martin

==================================================
1. Add Book
2. Show Books
3. Remove Book
4. Exit

Enter your choice (1-4): 3

Enter book title: Clean Code

Book removed successfully.

==================================================
1. Add Book
2. Show Books
3. Remove Book
4. Exit

Enter your choice (1-4): 2

Library Books
----------------------------------------
1. Python Crash Course - Eric Matthes

==================================================
1. Add Book
2. Show Books
3. Remove Book
4. Exit

Enter your choice (1-4): 4

Thank you for using Library Management System.
