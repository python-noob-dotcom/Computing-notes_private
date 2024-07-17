import sqlite3, flask
from flask import Flask, render_template, request

app = Flask(__name__)

# Routing to landing page for status entry
@app.route('/')
def home():
    return render_template('home.html')

# Routing to display page for employee records based on status entry
@app.route('/records', methods = ['POST'])
def emp_records():

    # Query to extract Sales dept records based on status provided
    query_sales = "SELECT Employee.Emp_ID, \
                        Employee.Emp_name, \
                        Employee.Dept, \
                        Employee.Emp_date, \
                        Sales.Sales \
                 FROM Employee, \
                      SALES \
                 WHERE Employee.Emp_ID = Sales.Emp_ID \
                 AND Employee.Status = ?"

    # Query to extract Tech dept records based on status provided 
    query_tech = "SELECT Employee.Emp_ID, \
                        Employee.Emp_name, \
                        Employee.Dept, \
                        Employee.Emp_date, \
                        Tech.Repairs \
                 FROM Employee, \
                      Tech \
                 WHERE Employee.Emp_ID = Tech.Emp_ID \
                 AND Employee.Status = ?"

    # Retrieve response submitted by user
    response = request.form['status']

    # Retrieve records based on response submitted by user
    with sqlite3.connect("records.db") as conn:

        cursor = conn.cursor()

        # Process user submission of status
        if response.upper() == 'CURRENT':
            status = 'Current'
        elif response.upper() == 'LEFT':
            status = 'Left'
        else:  # Error message if status submitted is invalid
            status = None
            error = 'Invalid status. Please enter Current of Left.'
            
        # Execute queries if status submitted is valid
        if status != None:

            values = (status,)

            
            try:
                # Retrieve Sales dept records
                cursor.execute(query_sales, values)
                results_sales = cursor.fetchall()

                # Retrieve Tech dept records
                cursor.execute(query_tech, values)
                results_tech = cursor.fetchall()


            except sqlite3.Error as e1:  # Capture sqlite3 errors
                    print(f'An SQLite error occured for Sales dept records: {e1}')
            except Exception as e2:  # Capture other code errors
                    print(f'An error occured: {e2}')

            # Further processing of retrived records
            results = []

            # Adjust Sales records to set value of 'NA' for Repairs made
            for record in results_sales:
                record = list(record)
                record.append('NA')
                results.append(record)

            # Adjust Tech records to set value of 'NA' for Sales made  
            for record in results_tech:
                record = list(record)
                record.insert(4, 'NA')
                results.append(record)

            # Sort results in ascending order of Emp_ID
            results.sort()

            # Render page to display retrieved records
            return render_template('records.html', status=status, results=results)
        
        # Render page to display error message if status submitted is invalid
        else:
            return render_template('records.html', status=status, error=error)

    # Connection automatically terminates upon exiting with block

if __name__ == '__main__':
    app.run()
