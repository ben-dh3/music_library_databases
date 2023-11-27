from lib.album import Album

class AlbumRepository:
    # Selecting all records
    # No arguments

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from albums')
        albums = []
        for row in rows:
            item = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(item)
        return albums

        # Executes the SQL query:
        # SELECT title, release_year, artist_id FROM albums;

        # Returns an array of album objects.

        # Gets a single record by its ID
        # One argument: the id (number)



    # def find(id):
    #     # Executes the SQL query:
    #     # SELECT title, release_year, artist_id FROM albums WHERE id = $1;

    #     # Returns a single album object.

    #     # Add more methods below for each operation you'd like to implement.

    # def create(title, release_year, artist_id):
    #     # INSERT INTO albums (title, release_year, artist_id) VALUES (<string>, <string>, <int>)
    #     # return None?

    # def update(optional arguments?)
    #     # UPDATE albums SET <argument> = ... WHERE <arguement> = ...
    #     # return None

    # def delete(optional arguments?)
    #     # DELETE FROM albums WHERE <arguments> = ...
    
