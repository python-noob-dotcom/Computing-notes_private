import sqlite3

with open(r'C:\Users\eugen\Desktop\Computing_notes\Computing-notes\Journey_to_A\Web_application\Web Applications Practice 1\DATA.txt', 'r') as f:
    members = []
    scores = []
    competition = []

    for line in f:
        line = line.strip().split(',')

        members += [(line[0], line[1], line[2])]
        scores += [(line[0], line[4], int(line[5]))]
        competition += [(line[4], line[3])]

member_query = "INSERT INTO Members(Mem_ID, Mem_Name, Mem_DOB) VALUES (?, ?, ?)"
competition_query = "INSERT INTO Competition(Comp_ID, Comp_Name) VALUES (?, ?)"
scores_query = "INSERT INTO Scores(Mem_ID, Comp_ID, Score) VALUES (?, ?, ?)"
members = list(set(members))
competition = list(set(competition))

with sqlite3.connect(r'C:\Users\eugen\Desktop\Computing_notes\Computing-notes\Journey_to_A\Web_application\Web Applications Practice 1\club.db') as conn:
    cursor = conn.cursor()

    for mem in members:
        cursor.execute(member_query, mem)
    for comp in competition:
        cursor.execute(competition_query, comp)
    for record in scores:
        cursor.execute(scores_query, record)
    
    conn.commit()