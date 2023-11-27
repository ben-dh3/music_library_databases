from lib.book import *

class BookRepository:
    def __init__(self, database_connection):
        self.database_connection = database_connection

    def all(self):
        rows = self.database_connection.execute('SELECT * FROM books')
        books = []
        for row in rows:
            item = Book(row['id'], row['title'], row['author_name'])
            books.append(item)

        return books