import flask
from flask import url_for
import sqlite3

app = flask.Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])

def landing():
    if flask.request.method == 'GET':
        return flask.render_template('TASK4_3_EUGENE_ANG.html')
    

            
    # string = ''
    # string += f'{"Name":<10}|{"Status":<10}\n'
    # string += '_'*20 + '\n'
    
    # for record in result:
    #     string += f'{record[0]:<10}|{record[1]:<10}\n'

@app.route('/result', methods = ['POST'])

def result():
    status = flask.request.form['record_type']
    with sqlite3.connect(r'C:\Users\eapar\OneDrive\Desktop\Computing-notes\Computing-notes\PAPERS\JC2_MYA\EUGENE_ANG_JIN_SENG\records.db') as conn:
        cursor = conn.cursor()
        
        if status not in ['Current', 'Left']:
            return 'error'

        if status == 'Current':
            results = cursor.execute('SELECT Emp_name, status, Dept, Emp_date, Sales FROM Employee WHERE Employee.status = "Current"')
        else:
            results = cursor.execute('SELECT Emp_name, status FROM Employee WHERE Employee.status = "Left"')
        global resulT
        resulT = results.fetchall()
    return flask.render_template('TASK4_3_RESULT.html', result = resulT)
    
    
if __name__ == '__main__':
    app.run(port = 888, debug = True)
    
    
