import sqlite3

"""
Concerned with storing and retrieving books from a database.

"""


def create_book_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')

    connection.commit()
    connection.close()


# add the book
def add_book(name, author):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    try:
        # Preventing sql intervention attacks
        cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))
    except:
        print("Book already exists in database!")

    connection.commit()
    connection.close()


# Show book list
def get_books():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM books')
    books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]  # will be received a
    # dictionary

    connection.close()

    return books


# If book is read
def mark_book_status(name, status):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    if status:
        cursor.execute('UPDATE books SET read=1 where name=?', (name,))
    else:
        cursor.execute('UPDATE books SET read=0 where name=?', (name,))

    connection.commit()
    connection.close()


# Delete book
def delete_book(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('DELETE FROM books WHERE name=?', (name,))

    connection.commit()
    connection.close()
