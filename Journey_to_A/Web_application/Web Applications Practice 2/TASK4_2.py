import sqlite3

with open(r'C:\Users\eugen\Desktop\Computing_notes\Computing-notes\Journey_to_A\Web_application\Web Applications Practice 2\Task4_2_2.txt', 'r') as f:
    sales = []
    for line in f:
        sales += [line.strip().split(',')]

with open(r'C:\Users\eugen\Desktop\Computing_notes\Computing-notes\Journey_to_A\Web_application\Web Applications Practice 2\Task4_2_1.txt', 'r') as f:
    tickets = []
    for line in f:
        tickets += [line.strip().split(',')]

ticket_query = "INSERT INTO Ticket VALUES (?, ?, ?, ?, ?)"
sales_query = "INSERT INTO Sale(saleID, tDate, quan, totalPrice) VALUES (?, ?, ?, ?)"

with sqlite3.connect(r'C:\Users\eugen\Desktop\Computing_notes\Computing-notes\Journey_to_A\Web_application\Web Applications Practice 2\MerlionThemePark.db') as conn:
    cursor = conn.cursor()

    for ticket in tickets:
        cursor.execute(ticket_query, (ticket[0], ticket[1], int(ticket[2]), int(ticket[3]), int(ticket[4])))
    for sale in sales:
        cursor.execute(sales_query, (int(sale[0]), sale[1], int(sale[2]), int(sale[3])))

    conn.commit()