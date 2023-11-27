from lib.book import Book

# We can format books to strings nicely

def format_book():
    book1 = Book(1, 'book name', 'author name')
    assert str(book1) == "Book(1, book name, author name"


'''
When I construct an Book
with the fields id, title and author_name
They are reflected in the instance properties
'''

def test_book_constructs():
    book = Book(1,'book name', 'author name')
    assert book.id == 1
    assert book.title == 'book name'
    assert book.author_name == 'author name'

# We can compare two identical books
# And have them be equal

def test_identical_books():
    book1 = Book(1, 'book name', 'author name')
    book2 = Book(1, 'book name', 'author name')
    assert book1 == book2


