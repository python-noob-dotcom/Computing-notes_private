# Task 4.1

import sqlite3

with sqlite3.connect(r'Computing-notes\Journey_to_A\Web_application\Web Applications Revision Practice 7\store.db') as conn:
    cursor = conn.cursor()

    cursor.execute("BEGIN TRANSACTION")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS "Donut" (
	"DonutID"	INTEGER,
	"DonutName"	TEXT,
	"UnitPrice"	REAL,
	PRIMARY KEY("DonutID")
    );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS "Member" (
	"MemberNumber"	INTEGER,
	"MemberName"	TEXT,
	"Phone"	INTEGER,
	PRIMARY KEY("MemberNumber")
    );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS "Sale" (
	"SaleID"	INTEGER,
	"MemberNumber"	INTEGER,
	"DonutID"	INTEGER,
	"Date"	TEXT,
	"Quantity"	INTEGER,
	PRIMARY KEY("SaleID"),
	FOREIGN KEY("MemberNumber") REFERENCES "Member"("MemberNumber"),
	FOREIGN KEY("DonutID") REFERENCES "Donut"("DonutID")
    );""")
    
    conn.commit()