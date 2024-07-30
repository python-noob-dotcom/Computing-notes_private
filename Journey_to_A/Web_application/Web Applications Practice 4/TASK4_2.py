import csv, sqlite3

with open(r'C:\Users\eugen\Desktop\Computing_notes\Computing-notes\Journey_to_A\Web_application\Web Applications Practice 4\ADDITIONS.CSV') as f:
    data = []
    reader = csv.reader(f)
    for line in reader:
        data += [line]

with sqlite3.connect(r'C:\Users\eugen\Desktop\Computing_notes\Computing-notes\Journey_to_A\Web_application\Web Applications Practice 4\TASK4.db') as conn:
    cursor = conn.cursor()
    cursor.execute("BEGIN TRANSACTION")
    query = "INSERT INTO TimeTable (event_id, date, time, venue) VALUES (?, ?, ?, ?)"
    for perf in data:
        event_id = int(cursor.execute("SELECT id FROM Event WHERE name = ?", (perf[0], )).fetchall()[0][0])
        cursor.execute(query, ([event_id, perf[2], perf[3], perf[4]]))

    conn.commit()