CREATE TABLE "Teacher" (
	"TeacherID"	INTEGER,
	"Name"	TEXT NOT NULL,
	"Department"	TEXT NOT NULL,
	"Contact"	TEXT NOT NULL,
	PRIMARY KEY("TeacherID" AUTOINCREMENT)
);

CREATE TABLE "Venue" (
	"VenueID"	INTEGER,
	"VenueName"	TEXT NOT NULL,
	"RoomNo"	TEXT NOT NULL,
	PRIMARY KEY("VenueID" AUTOINCREMENT)
);

CREATE TABLE "ExamSession" (
	"ExamSessionID"	INTEGER,
	"SubjectName"	TEXT NOT NULL,
	"PaperNo"	INTEGER NOT NULL,
	"VenueID"	TEXT NOT NULL,
	"Date"	TEXT NOT NULL,
	"StartTime"	TEXT NOT NULL,
	"EndTime"	TEXT NOT NULL,
	PRIMARY KEY("ExamSessionID" AUTOINCREMENT),
	FOREIGN KEY("VenueID") REFERENCES "Venue"("VenueID")
);

CREATE TABLE "ExamDuty" (
	"ExamSessionID"	INTEGER,
	"TeacherID"	INTEGER,
	"Role"	TEXT NOT NULL CHECK("Role" = 'PaperCoordinator' OR "Role" = 'Invigilator' OR "Role" = 'Relief' OR "Role" = 'RestroomDuty' OR "Role" = 'Reserve'),
	PRIMARY KEY("ExamSessionID","TeacherID"),
	FOREIGN KEY("TeacherID") REFERENCES "Teacher"("TeacherID"),
	FOREIGN KEY("ExamSessionID") REFERENCES "ExamSession"("ExamSessionID")
);