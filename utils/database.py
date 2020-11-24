"""

Concerned with storing and retrieving books from a csv file.
Format of the csv file:

name,author,read\n

"""

books_file = 'books.txt'


def create_book_table():
    with open(books_file, 'w') as file:
        pass # just to make sure that file is there

# add the book
def add_book(name, author):
    with open(books_file, 'a') as file:
        file.write(f'{name},{author},0\n')


# Show book list
def get_books():
    with open(books_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]

    return [
        {'name': line[0], 'author': line[1], 'read': line[2]}
        for line in lines
    ]


# If book is read
def mark_book_as_read(name):
    books = get_books()
    for book in books:
        if book['name'] == name:
            book['read'] = '1'
    _save_all_books(books)


def _save_all_books(books):
    with open(books_file, 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")


# Delete book
def delete_book(name):
    books = get_books()
    # add each book to the new list if book['name'] != # name
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)


