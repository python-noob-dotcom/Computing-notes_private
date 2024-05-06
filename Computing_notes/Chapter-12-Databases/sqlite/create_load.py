import sqlite3

conn = sqlite3.connect('library.db') # Load existing database or create a new database

conn.close() # Always close the connection when done