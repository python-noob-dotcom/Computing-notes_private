CREATE TABLE "Members" (
	"Mem_ID"	TEXT NOT NULL UNIQUE,
	"Mem_Name"	TEXT,
	"Mem_DOB"	TEXT,
	PRIMARY KEY("Mem_ID" AUTOINCREMENT)
);

CREATE TABLE "Competition" (
	"Comp_ID"	TEXT NOT NULL UNIQUE,
	"Comp_Name"	TEXT,
	PRIMARY KEY("Comp_ID")
);

CREATE TABLE "Scores" (
	"Mem_ID"	TEXT,
	"Comp_ID"	TEXT,
	"Score"	INTEGER,
	FOREIGN KEY("Mem_ID") REFERENCES "Members"("Mem_ID"),
	FOREIGN KEY("Comp_ID") REFERENCES "Competition"("Comp_ID"),
);