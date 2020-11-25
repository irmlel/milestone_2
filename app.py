from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'u' to mark a book as not read
- 'd' to delete a book
- 'q' to quit

Your choice:"""


def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'u':
            prompt_not_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Unknown command. Please try again.")
        user_input = input(USER_CHOICE)


# def prompt_add_book()  ask for book name and author
def prompt_add_book():
    book_name = input('Enter book name: ')
    book_author = input('Enter book author: ')

    database.add_book(book_name, book_author)


# def list_books()  show all the books in our list
def list_books():
    books = database.get_books()
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read}")


# def prompt_read_book() ask for book name and change it to "read" in our list
def prompt_read_book():
    book_name = input('Enter the book name you just finished reading: ')
    database.mark_book_status(book_name, True)


# def prompt_not_read_book() ask for book name and change it to "not read in our list"
def prompt_not_read_book():
    book_name = input('Enter the book name you are not read yet: ')
    database.mark_book_status(book_name, False)


# def prompt_delete_book() ask for book name and remove book from list
def prompt_delete_book():
    book_name = input('Enter the name of book you want to delete: ')

    database.delete_book(book_name)


# Run program
menu()





