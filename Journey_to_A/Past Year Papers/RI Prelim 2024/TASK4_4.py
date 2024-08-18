import flask, sqlite3

app = flask.Flask(__name__)

@app.route('/')

def home():
    return flask.render_template('index.html')

@app.route('/search')

def search():
    return flask.render_template('search.html')

@app.route('/result', methods = ['POST'])

def result(): 
    name = flask.request.form['name']
    date = flask.request.form['date']
    with sqlite3.connect(r'Computing-notes\Journey_to_A\Past Year Papers\RI Prelim 2024\datafiles\CLINIC.db') as conn:
        cursor = conn.cursor()
        query = 'SELECT AppointmentID, AppointmentDate, Patient.Name, Patient.PatientID, Staff.StaffID, Staff.Name, Diagnosis FROM Patient INNER JOIN (Appointment INNER JOIN Staff ON Appointment.StaffID = Staff.StaffID) ON Patient.PatientID = Appointment.PatientID WHERE Patient.Name = ? AND AppointmentDate = ?'
        result = cursor.execute(query, (name, date)).fetchall()

    return flask.render_template('result.html', result = result)

@app.route('/list')

def lst():
    with sqlite3.connect(r'Computing-notes\Journey_to_A\Past Year Papers\RI Prelim 2024\datafiles\CLINIC.db') as conn:
        cursor = conn.cursor()
        query = 'SELECT Staff.Name, Staff.Role, COUNT(Appointment.AppointmentID) FROM Staff \
        LEFT OUTER JOIN Appointment ON Appointment.StaffID = Staff.StaffID \
            GROUP BY Staff.Name ORDER BY COUNT(Appointment.AppointmentID)\
                DESC'
        
        result = cursor.execute(query).fetchall()

    return flask.render_template('staff_workload.html', result = result)

if __name__ == '__main__':
    app.run(debug = True)
