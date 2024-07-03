import sqlite3

with sqlite3.connect('library_2.db') as conn:
    cur = conn.cursor()

    try:
        cur.execute("BEGIN TRANSACTION")

        update = "UPDATE Book SET Title = 'Sample Book C' WHERE ID = 5"

        remove = "DELETE FROM Book WHERE ID = 9"
        # This form of statement is safer
        # cur.execute("DELETE FROM Book WHERE ID = ?", (9,))

        insert = "INSERT INTO Book (ID, Title) VALUES (1, 'Sample Book A')" # Make sure to check that the ID is not already in the table
                                                                            # Because the ID field is bounded by PRIMARY KEY which must
                                                                            # Be unique

        sql = [update, remove, insert]

        for query in sql:
            cur.execute(query)

        conn.commit()

    except sqlite3.Error:
        print('SQL error')
        conn.rollback()

    except:
        print('Regular error, check spelling')
        conn.rollback()
    
    finally:
        pass