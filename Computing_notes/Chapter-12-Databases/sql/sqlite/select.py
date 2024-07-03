# cursor.execute syntax:
# cursor.execute(query, values)

import sqlite3

lower = input("Enter lower limit: ")
upper = input("Enter upper limit: ")
with sqlite3.connect('library_2.db') as conn:
    cur = conn.cursor()

    try:
        sql_2 = "SELECT ID, Title FROM Book WHERE ID >= ? AND ID <= ?"
        conn.row_factory = sqlite3.Row
        results = cur.execute(sql_2, (int(lower), int(upper))).fetchall()

    except sqlite3.Error:
        print('SQL error')
        conn.rollback()
    
    except:
        conn.rollback()

for result in results:
    print(result)
