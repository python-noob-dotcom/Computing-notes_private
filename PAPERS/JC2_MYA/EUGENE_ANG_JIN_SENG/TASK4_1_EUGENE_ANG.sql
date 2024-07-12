BEGIN TRANSACTION;

CREATE TABLE `Employee` (
	`Emp_name`	TEXT NOT NULL,
	`Emp_ID`	INTEGER NOT NULL UNIQUE,
	`Dept`	TEXT,
	`Emp_date`	TEXT,
	`Status`	TEXT,
	PRIMARY KEY(`Emp_ID`)
);

CREATE TABLE `Sales` (
	`Emp_ID`	INTEGER,
	`Sales`	INTEGER,
	PRIMARY KEY(`Emp_ID`),
	FOREIGN KEY(`Emp_ID`) REFERENCES `Employee`(`Emp_ID`)
);

CREATE TABLE `Tech` (
	`Emp_ID`	INTEGER,
	`Repairs`	INTEGER,
	FOREIGN KEY(`Emp_ID`) REFERENCES `Employee`(`Emp_ID`),
	PRIMARY KEY(`Emp_ID`)
);

COMMIT; 
