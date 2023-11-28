from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.book_repository import BookRepository

# Connect to the database
connection = DatabaseConnection()
connection.connect()

# music_library seed

# Seed with some seed data
connection.seed("seeds/music_library.sql")

# # Retrieve all artists
# artist_repository = ArtistRepository(connection)
# artists = artist_repository.all()

artist_repository = ArtistRepository(connection)
artists = artist_repository.find()

# List them out
for artist in artists:
    print(artist)

# book_store seed

# # Seed with some seed data
# connection.seed("seeds/book_store.sql")

# # Retrieve all artists
# book_repository = BookRepository(connection)
# books = book_repository.all()

# # List them out
# for book in books:
#     print(book)
