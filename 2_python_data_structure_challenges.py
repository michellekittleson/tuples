'''
2. Python Data Structure Challenges in Real-World Scenarios

Task 1: Library System Enhancement

You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding new books and ensuring no duplicates.

Add functionality to insert new books into 'library'. Ensure that adding a duplicate book is handled appropriately.

'''


library = [
    ("1984", "George Orwell"),
    ("Brave New WOrld", "Aldous Huxley")
]

def insert_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    library.append((title, author))


def main():
    while True:
        print("\n1. Insert new book")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            insert_book()
        elif choice == '2':
            print("Exiting program.")
            break

main()