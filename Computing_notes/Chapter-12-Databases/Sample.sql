BEGIN TRANSACTION;
DROP TABLE IF EXISTS `Subjects`;
CREATE TABLE IF NOT EXISTS `Subjects` (
	`subject_name`	TEXT,
	`no_students`	INTEGER,
	`cls`	TEXT,
	PRIMARY KEY(`subject_name`),
	FOREIGN KEY(`cls`) REFERENCES `Students`(`cls`)
);
DROP TABLE IF EXISTS `Students`;
CREATE TABLE IF NOT EXISTS `Students` (
	`NRIC`	TEXT,
	`Name`	TEXT,
	`cls`	TEXT,
	`DoB`	TEXT,
	PRIMARY KEY(`NRIC`,`cls`)
);
COMMIT;
