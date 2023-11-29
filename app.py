from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
import sys
# from lib.book_repository import BookRepository

class Application():
    def __init__(self):
        # Connect to the database
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")

    def run(self):
        # "Runs" the terminal application.
        # It might:
        #   * Ask the user to enter some input
        #   * Make some decisions based on that input
        #   * Query the database
        #   * Display some output
        # We're going to print out the artists!

        self.write("Welcome to the music library manager!\n")
        self.write("What would you like to do?\n")
        input = self._prompt("1 - List all albums \n2 - List all artists\n\nEnter your choice: ")
        if input == "1":
            album_repository = AlbumRepository(self._connection)
            # Retrieve all artists
            albums = album_repository.all()
            for album in albums:
                print(f"{album.id}: {album.title} {album.release_year} ({album.artist_id})")
        if input == "2":
            artist_repository = ArtistRepository(self._connection)
            # Retrieve all artists
            artists = artist_repository.all()
            for artist in artists:
                print(f"{artist.id}: {artist.name} ({artist.genre})")

    def _prompt(self, message):
        self.write(message + "\n")
        return self.readline().strip()
    
    def write(self, message):
        sys.stdout.write(message +"\n")

    def readline(self):
        return sys.stdin.readline()


if __name__ == '__main__':
    app = Application()
    app.run()

# other functions and book repository:

# artist_repository = ArtistRepository(connection)
# artists = artist_repository.find()
# # List them out
# for artist in artists:
#     print(artist)

# book_store seed

# # Seed with some seed data
# connection.seed("seeds/book_store.sql")

# # Retrieve all artists
# book_repository = BookRepository(connection)
# books = book_repository.all()

# # List them out
# for book in books:
#     print(book)
