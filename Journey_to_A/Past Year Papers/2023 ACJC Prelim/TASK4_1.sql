BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS "Members" (
	"Mem_ID"	TEXT,
	"Mem_Name"	TEXT,
	"Mem_DOB"	INTEGER,
	PRIMARY KEY("Mem_ID")
);

CREATE TABLE IF NOT EXISTS "Competitions" (
	"Comp_ID"	TEXT,
	"Comp_Name"	TEXT,
	PRIMARY KEY("Comp_ID")
);

CREATE TABLE IF NOT EXISTS "Scores" (
	"Mem_ID"	TEXT,
	"Comp_ID"	TEXT,
	"Comp_Score"	INTEGER,
	FOREIGN KEY("Mem_ID") REFERENCES "Members"("Mem_ID"),
	FOREIGN KEY("Comp_ID") REFERENCES "Competitions"("Comp_ID"),
	PRIMARY KEY("Mem_ID","Comp_ID")
);

COMMIT;