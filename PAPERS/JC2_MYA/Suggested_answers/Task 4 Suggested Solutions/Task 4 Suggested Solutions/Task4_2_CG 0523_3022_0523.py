import sqlite3

# Process data in SALES.txt into sales master list
sales = []
with open("./SALES.txt","r") as f:
    for line in f:
        record = line.strip().split(',')
        sales.append(record)

# Process data in TECH.txt into tech master list
tech = []
with open("./TECH.txt", "r") as f:
    for line in f:
        record = line.strip().split(',')
        tech.append(record)

# INSERT statement for records in sales dept to Employee table
query_emp = "INSERT INTO Employee(Emp_name, \
                               Emp_ID, \
                               Dept, \
                               Emp_date, \
                               Status) \
             VALUES (?, ? , ? , ?, ?)"

# INSERT statement for records in sales dept to Sales table
query_sales = "INSERT INTO Sales(Emp_ID, \
                                 Sales) \
               VALUES (?, ?)"

# INSERT statement for records in sales dept to Tech table
query_tech = "INSERT INTO Tech(Emp_ID, \
                               Repairs) \
              VALUES (?, ?)"


with sqlite3.connect("records.db") as conn:  # Establish connection
    cursor = conn.cursor()

    # Identify values for each Sales dept record to be inserted
    for record in sales:
        Emp_ID = int(record[0])
        Emp_name = record[1]
        Emp_date = record[2]
        Status = record[3]
        Sales = record[4]

        # Values to be inserted into Employee table 
        values_emp = (Emp_name, \
                      Emp_ID, \
                      "Sales", \
                      Emp_date, \
                      Status)

        # Values to be inserted into Sales table
        values_sales = (Emp_ID, \
                        Sales)

        # Perform insertion
        try:
            cursor.execute(query_emp, values_emp)
            cursor.execute(query_sales, values_sales)
        except sqlite3.Error as e1:  # Capture sqlite3 errors
            print(f'An SQLite error occured for Sales dept records: {e1}')
        except Exception as e2:  # Capture other code errors
            print(f'An error occured: {e2}')

    conn.commit() # Commit addition of Sales dept records

    # Identify values for each Tech dept record to be inserted
    for record in tech:
        Emp_ID = int(record[0])
        Emp_name = record[1]
        Emp_date = record[2]
        Status = record[3]
        Repairs = int(record[4])

        # Values to be inserted into Employee table
        values_emp = (Emp_name, \
                      Emp_ID, \
                      "Tech", \
                      Emp_date, \
                      Status)

        # Values to be inserted into Tech table
        values_tech = (Emp_ID, \
                       Repairs)

        # Perform insertion
        try:
            cursor.execute(query_emp, values_emp)
            cursor.execute(query_tech, values_tech)
        except sqlite3.Error as e1:  # Capture sqlite3 errors
            print(f'An SQLite error occured Tech dept records: {e1}')
        except Exception as e2:  # Capture other code errors
            print(f'An error occured: {e2}')

    conn.commit()  # Commit addition of Tech dept records

# Connection automatically terminates upon exiting with block
