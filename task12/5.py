'''Write a python program that allows a librarian to add several books to a libraray. For each book , ask 
the user to enter its title and the number of copies. Store each book and its available copy count in a dictionary.
After the books have been added, display a menu that lets the user issue a book, return a book, display all books, or exit the program.
Apply these conditions:
-Book titles should be compared without dsitinguishing uppercase and lowercase letters.
-A book can be issued only if it exists in the library and at least one copy is available.
-Issuing a book decreases its available copy count by one.
-A book can be returned only if it exists in the library and at least one copy has already been issued.
-Returning a book increases its available copy count by one.
-Display an appropriate message for an unavailable book, an invaild choice, or an invalid number of copies.'''

# Library data store karne ke liye dictionaries
# library: Isme current available copies hongi
# max_copies: Isme shuruat ki total copies hongi taaki return ka check lag sake
library = {}
max_copies = {}


print("--- Add Books to the Library ---")
while True:
    title = input("Enter book title (or type 'done' to finish): ").strip()
    if title.lower() == 'done':
        break
        
    if not title:
        print("Error: Book title cannot be empty!")
        continue
        
    try:
        copies = int(input(f"Enter number of copies for '{title}': "))
        if copies <= 0:
            print("Error: Invalid number of copies! Must be greater than 0.")
            continue
    except ValueError:
        print("Error: Invalid input! Please enter a valid integer number.")
        continue

    
    title_lower = title.lower()
    
    if title_lower in library:
        library[title_lower] += copies
        max_copies[title_lower] += copies
    else:
        library[title_lower] = copies
        max_copies[title_lower] = copies
    print(f"Success: Added {copies} copies of '{title}'.\n")

# 2. Menu driven system
while True:
    print("\n--- Library Menu ---")
    print("1. Issue a Book")
    print("2. Return a Book")
    print("3. Display All Books")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ").strip()
    
    # Condition: Issue a Book
    if choice == '1':
        title = input("Enter the title of the book to issue: ").strip().lower()
        if title in library:
            if library[title] > 0:
                library[title] -= 1
                print("Success: Book issued successfully!")
            else:
                print("Error: Out of stock! No copies available right now.")
        else:
            print("Error: This book is unavailable in the library.")
            
    # Condition: Return a Book
    elif choice == '2':
        title = input("Enter the title of the book to return: ").strip().lower()
        if title in library:
            # Check ki kya koi copy already issue hui thi (available < max)
            if library[title] < max_copies[title]:
                library[title] += 1
                print("Success: Book returned successfully!")
            else:
                print("Error: All copies are already in the library. This book wasn't issued from here!")
        else:
            print("Error: This book does not belong to this library.")
            
    # Condition: Display All Books
    elif choice == '3':
        if not library:
            print("The library is currently empty.")
        else:
            print("\nAvailable Books in Library:")
            for book, count in library.items():
                print(f"- {book.title()}: {count} copies available")
                
    
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
        
    
    else:
        print("Error: Invalid choice! Please enter a number between 1 and 4.")