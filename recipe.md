table: album

Columns:
title | release_year | artist_id


<!-- -->



'''
Book
BookRepository
'''
class Book:
    def __init__(self, title, author_name):
        pass

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Book({self.id}, {self.title}, {self.author_name}"
    
class BookRepository:
    def __init__(self, database_connection):
        pass

    def all(self):
        pass


# Tests - Book


'''
When I construct an Book
with the fields id, title and author_name
They are reflected in the instance properties
'''

"""
We can compare two identical books
And have them be equal
"""

"""
We can format books to strings nicely
"""

# Tests - BookRepository - all()

"""
When we call AlbumRepository#all
We get a list of Album objects reflecting the seed data.
"""

# small function in app.py

'''
# Retrieve all albums
book_repository = BookRepository(connection)
albums = album_repository.all()

# List them out
for book in books:
    print(book)

'''
