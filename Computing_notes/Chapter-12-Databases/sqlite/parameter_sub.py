# cursor.execute syntax:
# cursor.execute(query, values)

import sqlite3

id = input("Enter id of new book: ")
title = input("Enter title of new book: ")
lower = input("Enter lower limit: ")
upper = input("Enter upper limit: ")
with sqlite3.connect('library_2.db') as conn:
    cur = conn.cursor()

    try:
        cur.execute("BEGIN TRANSACTION")
        sql = "INSERT INTO Book(ID, Title) VALUES (?, ?)"
        sql_2 = "SELECT FROM Book (Title) WHERE ID > ? AND ID < ?"
        

        cur.execute(sql, (int(id), title))
        results = cur.execute(sql_2, (int(lower), int(upper))).fetchall()
        conn.commit()

    except sqlite3.Error:
        print('SQL error')
        conn.rollback()
    
    except:
        conn.rollback()

