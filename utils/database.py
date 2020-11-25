import json

"""
Concerned with storing and retrieving books from a json file.

[
    {
        'name': 'Book name',
        'author': 'Book author',
        'read': False
    }

]
"""

books_file = 'books.json'


def create_book_table():
    with open(books_file, 'w') as file:
        json.dump([], file)


# add the book
def add_book(name, author):
    books = get_books()
    books.append({'name': name, 'author': author, 'read': False})
    _save_all_books(books)


# Show book list
def get_books():
    with open(books_file, 'r') as file:
        return json.load(file)


def _save_all_books(books):
    with open(books_file, 'w') as file:
        json.dump(books, file)


# If book is read
def mark_book_as_read(name):
    books = get_books()
    for book in books:
        if book['name'] == name:
            book['read'] = True
    _save_all_books(books)


# Delete book
def delete_book(name):
    books = get_books()
    # add each book to the new list if book['name'] != # name
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)


