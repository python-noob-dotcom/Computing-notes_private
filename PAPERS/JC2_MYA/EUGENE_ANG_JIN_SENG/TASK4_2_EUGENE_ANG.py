import sqlite3

with open('./SALES.txt', 'r') as sales:
    sale = []
    for line in sales:
        sale += [line.strip().split(',')]
        
with open('./TECH.txt', 'r') as techs:
    tech = []
    for line in techs:
        tech += [line.strip().split(',')]

with sqlite3.connect('./records.db') as conn:
    cursor = conn.cursor()
    
    cursor.execute('BEGIN TRANSACTION')
    
    for employee in sale:
        cursor.execute("INSERT INTO Employee VALUES (?, ?, 'Sales', ?, ?)", (employee[1], employee[0], employee[2], employee[3]))
        cursor.execute("INSERT INTO Sales VALUES (?, ?)", (employee[0], int(employee[4])))
    
    for employee in tech:
        cursor.execute("INSERT INTO Employee VALUES (?, ?, 'Tech', ?, ?)", (employee[1], employee[0], employee[2], employee[3]))
        cursor.execute("INSERT INTO Tech VALUES (?, ?)", (employee[0], int(employee[4])))
    
    conn.commit()
