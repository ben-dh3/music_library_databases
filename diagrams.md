# diagram.codes
# album repository diagram

alias terminal="terminal"
alias app.py="app.py"
alias album_repository="album_repository"
alias database_connection="database_connection"
alias postgres_database="postgres_database"

terminal->app.py: "Runs 'python app.py'"
app.py->album_repository: "Calls 'all' method on album repository"
app.py->database_connection: "Opens connection to database by calling connect method on database connection class"
database_connection->database_connection: "Opens database connection using PG and stores the connection"
album_repository->database_connection: "Sends SQL query by calling execute method on database connection"
database_connection->postgres_database: "Sends query to database via the open database connection."
postgres_database->database_connection: "Returns a list of dictionaries one for each row of the albums table"
database_connection->album_repository: "Returns a list of dictionaries one for each row of the albums table"
album_repository->album_repository: "Loops through list and creates a album object for every row"
album_repository-> app.py: "Returns a list of album objects"
app.py->terminal: "Prints list of objects to terminal"


# book repository diagram

alias terminal="terminal"
alias app.py="app.py"
alias book_repository="book_repository"
alias database_connection="database_connection"
alias postgres_database="postgres_database"

terminal->app.py: "Runs 'python app.py'"
app.py->book_repository: "Calls 'all' method on book_repository class"
app.py->database_connection: "Opens connection to database by calling connect method on database connection class"
database_connection->database_connection: "Opens database connection using postgres and stores the connection"
book_repository->database_connection: "Sends SQL query by calling execute method on database connection"
database_connection->postgres_database: "Sends query to database via the open database connection."
postgres_database->database_connection: "Returns a list of dictionaries one for each row of the books table"
database_connection->book_repository: "Returns a list of dictionaries one for each row of the books table"
book_repository->book_repository: "Loops through list and creates a book object for every row"
book_repository-> app.py: "Returns a list of book objects"
app.py->terminal: "Prints list of objects to terminal"
