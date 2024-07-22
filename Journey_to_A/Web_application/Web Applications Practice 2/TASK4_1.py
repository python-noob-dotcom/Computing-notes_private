import sqlite3

with sqlite3.connect(r'C:\Users\eugen\Desktop\Computing_notes\Computing-notes\Journey_to_A\Web_application\Web Applications Practice 2\MerlionThemePark.db') as conn:
    cursor = conn.cursor()

    cursor.execute("BEGIN TRANSACTION")
    cursor.execute('CREATE TABLE "Ticket" (\
	"Date"	TEXT UNIQUE,\
	"dayOfWeek"	TEXT,\
	"unitPrice"	INTEGER,\
	"totQuan"	INTEGER,\
	"availQuan"	INTEGER,\
	PRIMARY KEY("Date")\
    );')

    cursor.execute('CREATE TABLE "Sale" (\
	"saleID"	INTEGER UNIQUE,\
	"tDate"	INTEGER,\
	"quan"	INTEGER,\
	"totalPrice"	INTEGER,\
	FOREIGN KEY("tDate") REFERENCES "Ticket"("Date"),\
	PRIMARY KEY("saleID" AUTOINCREMENT)\
    );')

    conn.commit()