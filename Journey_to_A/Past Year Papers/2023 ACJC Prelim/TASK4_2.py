import sqlite3

with open(r'Computing-notes\Journey_to_A\Past Year Papers\2023 ACJC Prelim\DATA.txt') as f:
    data = []
    mems = []
    comps = []
    for line in f:
        line = line.strip().split(',')
        data += [line]
        mems += [(line[0], line[1], line[2])]
        comps += [(line[4], line[3])]
        

with sqlite3.connect(r'Computing-notes\Journey_to_A\Past Year Papers\2023 ACJC Prelim\club.db') as conn:
    cursor = conn.cursor()

    cursor.execute("BEGIN TRANSACTION")
    mem = "INSERT INTO Members VALUES (?, ?, ?)"
    comp = "INSERT INTO Competitions VALUES (?, ?)"
    score = "INSERT INTO Scores VALUES (?, ?, ?)"

    for memb in mems:
        cursor.execute(mem, memb)
    
    for compe in comps:
        cursor.execute(comp, compe)

    for rec in data:
        cursor.execute(score, (rec[0], rec[4], rec[5]))

    conn.commit()