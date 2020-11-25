from .database_connection import DatabaseConnection

"""
Concerned with storing and retrieving books from a database.

"""


def create_book_table():
    with DatabaseConnection('data.db') as cursor:

        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')


# add the book
def add_book(name, author):
    with DatabaseConnection('data.db') as cursor:
        try:
            # Preventing sql intervention attacks
            cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))
        except:
            print("Book already exists in database!")


# Show book list
def get_books():
    with DatabaseConnection('data.db') as cursor:
        cursor.execute('SELECT * FROM books')
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]  # will be received a
        # dictionary

    return books


# If book is read
def mark_book_status(name, status):
    with DatabaseConnection('data.db') as cursor:
        if status:
            cursor.execute('UPDATE books SET read=1 where name=?', (name,))
        else:
            cursor.execute('UPDATE books SET read=0 where name=?', (name,))


# Delete book
def delete_book(name):
    with DatabaseConnection('data.db') as cursor:

        cursor.execute('DELETE FROM books WHERE name=?', (name,))
