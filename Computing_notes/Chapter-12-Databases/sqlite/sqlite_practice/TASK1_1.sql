BEGIN TRANSACTION

CREATE TABLE `Device` (
	`serial_number`	INTEGER UNIQUE,
	`type`	TEXT,
	`model`	TEXT,
	`location`	TEXT,
	`date_of_purchase`	NUMERIC,
	`written_off`	TEXT,
	PRIMARY KEY(`serial_number`)
);

CREATE TABLE `Monitor` (
	`serial_number`	INTEGER,
	`date_cleaned`	NUMERIC,
	PRIMARY KEY(`serial_number`),
	FOREIGN KEY(`serial_number`) REFERENCES `Device`(`serial_number`)
);

CREATE TABLE `Laptop` (
	`serial_number`	INTEGER,
	`weight_kg`	INTEGER,
	PRIMARY KEY(`serial_number`),
	FOREIGN KEY(`serial_number`) REFERENCES `Device`(`serial_number`)
);

CREATE TABLE `Printer` (
	`serial_number`	INTEGER,
	`toner`	TEXT,
	`date_changed` NUMERIC,
	PRIMARY KEY(`serial_number`),
	FOREIGN KEY(`serial_number`) REFERENCES `Device`(`serial_number`)
);

COMMIT;

