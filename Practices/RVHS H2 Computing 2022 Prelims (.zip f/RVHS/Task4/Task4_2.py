import csv
import os
import sqlite3

curr_dir = os.path.dirname(os.path.abspath(__file__))
db_file = os.path.join(curr_dir, "invigilation.db")

table_names = ["Teacher", "Venue", "ExamSession", "ExamDuty"]


def read_file():
    for i in range(len(table_names)):
        db = sqlite3.connect(db_file)
        file_name = os.path.join(
            curr_dir, "data_files/{}.csv".format(table_names[i]))

        with open(file_name, "r") as f:
            csv_reader = csv.reader(f)
            header = next(csv_reader)

            for row in csv_reader:
                query = "INSERT INTO {} {} VALUES ({})".format(
                    table_names[i],
                    tuple(header),
                    ("?,"*len(header))[:-1])

                db.execute(query, tuple(row))

        db.commit()
        db.close()


read_file()
