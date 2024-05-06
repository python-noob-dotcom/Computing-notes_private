import sqlite3

conn = sqlite3.connect('library.db') # Connection class object created - connected to the database

cursor = conn.cursor()
# cursor class object created - lets you create a database cursor to use SQL statements and fetch result - contains fetch method etc.

# SQL Statement

statement = "CREATE TABLE BOOK \
    (ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    Title TEXT)"

cursor.execute(statement)

# Always commit to save the changes
conn.commit()


# Always remember to close the connection
conn.close()


# with sqlite3.connect('library.db') as connection:
    # cur = connection.cursor()

    #...

    # file auto closes.
