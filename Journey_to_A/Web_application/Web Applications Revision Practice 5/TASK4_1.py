import sqlite3

with sqlite3.connect(r'Computing-notes\Journey_to_A\Web_application\Web Applications Revision Practice 5\Taxi.db') as conn:
    cursor = conn.cursor()

    cursor.execute("BEGIN TRANSACTION")
    cursor.execute("""
    CREATE TABLE "Feedback" (
        "ID"	INTEGER,
        "Driver_ID"	INTEGER,
        "Date"	TEXT,
        "Comment"	TEXT,
        FOREIGN KEY("Driver_ID") REFERENCES "Driver"("ID"),
        PRIMARY KEY("ID" AUTOINCREMENT)
    );
    """)

    with open(r'Computing-notes\Journey_to_A\Web_application\Web Applications Revision Practice 5\Feedback.txt', 'r') as f:
        feedbacks = []

        for line in f:
            feedbacks += [line.strip().split(',')]

    feedbacks = feedbacks[1:]
    for feedback in feedbacks:
        cursor.execute("INSERT INTO Feedback (Driver_ID, Date, Comment) VALUES (?, ?, ?)",
                    (feedback[0], feedback[1], feedback[2]))
        

    

    conn.commit()

